import os
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "notes_db")

client: MongoClient = None
database: Database = None

def connect_to_mongodb():
    """
    Establish connection to MongoDB database
    """
    global client, database
    try:
        client = MongoClient(MONGO_URI)
        database = client[DATABASE_NAME]
        client.server_info()
        print(f"Successfully connected to MongoDB database: {DATABASE_NAME}")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e


def close_mongodb_connection():
    """
    Close MongoDB connection
    """
    global client
    if client:
        client.close()
        print("MongoDB connection closed")


def get_database() -> Database:
    """
    Get the database instance
    """
    return database


def get_collection(collection_name: str) -> Collection:
    """
    Get a specific collection from the database
    
    Args:
        collection_name: Name of the collection to retrieve
        
    Returns:
        MongoDB collection instance
    """
    return database[collection_name]