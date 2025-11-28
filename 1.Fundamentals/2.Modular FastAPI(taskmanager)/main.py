from fastapi import FastAPI
from routes.task import router as tasks_router

app = FastAPI()

app.include_router(tasks_router)

@app.get("/")
def home():
    return {"message": "Task Manager API Running"}
