from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.notes_routes import router as notes_router

app = FastAPI(title="Notes API with Auth & Roles")

app.include_router(auth_router)
app.include_router(notes_router)
