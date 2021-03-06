import os
import psycopg2
import bmemcached
from flask import Flask
from flask_cors import CORS
import googleapiclient.discovery

__all__ = ["cur", "app", "mc", "youtube", "YOUTUBE_CHANNEL"]

DATABASE_URL = os.environ["DATABASE_URL"]
YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]
YOUTUBE_CHANNEL = os.environ["YOUTUBE_CHANNEL_ID"]

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

mc = bmemcached.Client(
    os.environ.get("MEMCACHEDCLOUD_SERVERS").split(","),
    os.environ.get("MEMCACHEDCLOUD_USERNAME"),
    os.environ.get("MEMCACHEDCLOUD_PASSWORD"),
)

app = Flask(__name__)
cors = CORS(app)

# Init routes
from . import routes
