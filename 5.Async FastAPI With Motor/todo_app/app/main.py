from fastapi import FastAPI
from app.routes import auth_routes
from app.routes import todo_routes

app=FastAPI(title="Todo App",description="Todo App",version="0.0.1")

app.include_router(auth_routes.router)
app.include_router(todo_routes.router)

@app.get('/')
def read_root():
    return {"status": "success! Welcome to the Todo App"}