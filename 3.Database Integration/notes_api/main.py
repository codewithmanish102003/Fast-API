from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from database.mongodb import connect_to_mongodb, close_mongodb_connection
from routes.notes import router as notes_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events
    """
    connect_to_mongodb()
    yield
    close_mongodb_connection()

app = FastAPI(
    title="Notes API",
    description="A simple Notes API with MongoDB integration",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(notes_router)

@app.get("/")
def root():
    """
    Root endpoint
    """
    return {
        "message": "Welcome to Notes API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "service": "notes-api"
    }