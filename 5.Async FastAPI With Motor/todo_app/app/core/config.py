import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017/todo_db")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "todo_db")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "secret")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
settings=Settings()
