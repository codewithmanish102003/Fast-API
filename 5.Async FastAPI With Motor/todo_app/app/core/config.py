import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    MONGO_URI:str=os.getenv("MONGO_URI")
    DATABASE_NAME:str=os.getenv("DATABASE_NAME")
    JWT_SECRET_KEY:str=os.getenv("JWT_SECRET_KEY")
    ALGORITHM:str=os.getenv("ALGORITHM")
   
settings=Settings()
