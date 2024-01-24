#activate env source tg-panel/bin/activate tg-panel
from quart import Quart, request, jsonify, render_template
from motor.motor_asyncio import AsyncIOMotorClient
from bson.json_util import dumps
import colorsys
from collections import Counter
import asyncio
import os
from hypercorn.config import Config
from hypercorn.asyncio import serve
from datetime import datetime, timedelta
import aioredis

uri = os.getenv("MONGODB_URI")
client = AsyncIOMotorClient(uri)
mydb = client['posts']
db = mydb["telegram"]
posts = db.posts
app = Quart(__name__)

ALLOWED_HOURS = [6, 12, 24, 48]
START_COLOR = (255, 0, 0)
END_COLOR = (0, 0, 0)


async def prepare_data(db,hours):
    time_ago = datetime.now() - timedelta(hours=hours)
    pipeline = [
        {"$match": {
            "region": {"$ne": None},
            "date": {"$gte": time_ago}
        }},
        {"$group": {
            "_id": "$region",
            "records": {
                "$push": {
                    "date": "$date",
                    "words": "$words",
                    "message_id": "$message_id",
                    "_id": "$_id",
                    "source": "$source",
                    "text": "$text",
                    "channel_id": "$channel_id",
                    "channel_username": "$channel_username"
                }
            },
            "numRecords": {"$sum": 1}
        }},
        {"$sort": {"numRecords": -1}}
    ]

    results = await db.aggregate(pipeline).to_list(None)
    regions = [doc['_id'] for doc in results]
    all_words = " ".join([" ".join(record['words']) for region in results for record in region['records']])

    word_counts = Counter(all_words.split())
    top_words = word_counts.most_common(6)

    max_num_records = max([doc['numRecords'] for doc in results], default=1)

    region_colors = {}
    start_color = (255, 0, 0)  
    end_color = (0, 0, 0)  
    start_hsv = colorsys.rgb_to_hsv(*start_color)
    end_hsv = colorsys.rgb_to_hsv(*end_color)
    
    for region in regions:
        index = regions.index(region)
        relative_position = index / len(regions)
        new_hsv = tuple(start + relative_position * (end - start) for start, end in zip(start_hsv, end_hsv))
        color = colorsys.hsv_to_rgb(*new_hsv)
        region_colors[region] = {'color': color}

    region_news = {}
    region_counts = {}
    for region in regions:
        region_news[region] = await db.find({"region": region}).sort([("date", -1)]).to_list(10)
        region_counts[region] = await db.count_documents({"region": region})
    region_news = {k: v for k, v in sorted(region_news.items(), key=lambda item: region_counts[item[0]], reverse=True)}
    
    return regions, region_colors, region_news, region_counts, top_words


@app.before_serving
async def create_redis_pool():
    global redis
    redis_url = os.getenv('REDIS_URL', 'redis://localhost')
    redis = await aioredis.from_url(redis_url)

@app.route('/')
async def main():
    try:
        hours = request.args.get('hours', default=6, type=int)
        if hours not in ALLOWED_HOURS:
            return "Invalid hours value. It should be one of the following: {}.".format(", ".join(map(str, ALLOWED_HOURS))), 400

        cached_data = await redis.get(f'cached_data_{hours}')
        if cached_data is not None:
            print("Using cached data")
            return cached_data

        regions, region_colors, region_news, region_counts, top_words = await prepare_data(db=db,hours=hours)

        response = await render_template('index.html', hours=hours, regions=region_colors, news=region_news, counts=region_counts, top_words=top_words)
        response_data = response 

        await redis.setex(f'cached_data_{hours}', 600, response_data)
        return response
    except Exception as e:
        return str(e), 500

@app.route('/search', methods=['GET'])
async def search():
    query = request.args.get('q', '')
    await db.create_index([("text", "text")])
    results = await db.find({"$text": {"$search": query}}).to_list(None)
    return await render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    config = Config()
    config.bind = [os.getenv("BIND_ADDRESS")]
    asyncio.run(serve(app, config))