from pyrogram import Client, filters, types
from pymongo import MongoClient
import re
import os
from datetime import datetime
from region import get_region
from words import keywords

app = Client(
    "client2", 
    api_id = os.getenv("TELEGRAM_API_ID"), 
    api_hash = os.getenv("TELEGRAM_API_HASH")
)

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)
mydb = client['posts']
db = mydb["telegram"]
posts = db.posts

@app.on_message(filters.channel)
def handle_channel_post(client, message):
   if message.text:
       parse_words(message)
   elif message.poll:
       handle_poll(message)
   elif message.media:
       handle_media(message)
   else:
       print("Message incorrect")


def handle_poll(message):
   poll_data = {
       'channel_id': message.chat.id,
       'message_id': message.id,
       'date': message.date,
       #'poll': message.poll.to_dict()
   }
   print(poll_data)
   x = db.insert_one(poll_data)

def handle_media(message):
   media_data = {
       'source': 'telegram',
       'channel_id': message.chat.id,
       'message_id': message.id,
       'date': message.date,
       'text': message.caption,
       'region': get_region(message.caption),
       'words': keywords(message.caption)
       #'media': message.media.to_dict()
   }
   print(media_data)
   x = db.insert_one(media_data)

def parse_words(message):
    media_data = {
       'source': 'telegram',
       'channel_id': message.chat.id,
       'channel_username': message.chat.username,
       'message_id': message.id,
       'date': message.date,
       'text': message.text,
       'region': get_region(message.text),
       'words': keywords(message.text)
   }
    print(media_data)
    x = db.insert_one(media_data)

app.run()