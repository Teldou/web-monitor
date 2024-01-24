import pytest
from quart.testing import QuartClient
from app import app, prepare_data
import mongomock
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

@pytest.fixture
def client():
    return QuartClient(app)

@pytest.fixture
def mongodb():
    client = mongomock.MongoClient()
    mydb = client['test_db']
    return mydb["telegram"]

@pytest.mark.asyncio
async def test_main_route(client):
    response = await client.get('/')
    assert response.status_code == 200

    soup = BeautifulSoup(await response.data.decode(), 'html.parser')
    top_words = soup.find_all('div', class_='bg-white shadow-md rounded p-4')
    for word_div in top_words:
        word, count = word_div.text.strip().split(': ')
        assert word in ["test", "words"]
        assert int(count) > 0

@pytest.mark.asyncio
async def test_search_route(client):
    response = await client.get('/search?q=test')
    assert response.status_code == 200

    soup = BeautifulSoup(await response.data.decode(), 'html.parser')
    regions = soup.find_all('div', class_='region-block bg-white shadow-md rounded p-6 w-full md:w-1/2 xl:w-1/3 m-2')
    for region_div in regions:
        region_name = region_div.find('h2').text.split(' ')[0]
        assert region_name == "test_region"

@pytest.mark.asyncio
async def test_prepare_data(mongodb):
    # Insert some mock data into the database
    now = datetime.now()
    hours_ago = now - timedelta(hours=6)
    mongodb.insert_one({
        "region": "test_region",
        "date": hours_ago,
        "words": ["test", "words"],
        "message_id": "test_message_id",
        "_id": "test_id",
        "source": "test_source",
        "text": "test text",
        "channel_id": "test_channel_id",
        "channel_username": "test_channel_username"
    })

    # Test the prepare_data function
    regions, region_colors, region_news, region_counts, top_words = await prepare_data(mongodb, 6)
    assert regions == ["test_region"]
    assert "test_region" in region_colors
    assert "test_region" in region_news
    assert "test_region" in region_counts
    assert region_counts["test_region"] == 1
    assert top_words == [("test", 2), ("words", 1)]