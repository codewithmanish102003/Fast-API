from typing import Optional

from pymongo import MongoClient

from .config import settings


class MongoDB:
    client: Optional[MongoClient] = None
    db = None


mongodb = MongoDB()


def connect():
    if mongodb.client is None:
        mongodb.client = MongoClient(settings.mongodb_url)
        mongodb.db = mongodb.client[settings.mongodb_db]
    return mongodb.db


def close():
    if mongodb.client is not None:
        mongodb.client.close()
        mongodb.client = None
        mongodb.db = None
