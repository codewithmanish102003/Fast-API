from core.config import settings
from core.database import close, connect
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from routes import notes, users

# Configure OAuth2 security scheme
oauth2_scheme = OAuth2(
    flows=OAuthFlowsModel(
        password={
            "tokenUrl": "/users/login",
            "scopes": {}
        }
    ),
    auto_error=False
)

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    connect()


@app.on_event("shutdown")
def on_shutdown():
    close()


@app.get("/")
def root():
    return {"message": "Welcome to the Authentication & Authorization API", "docs": "/docs"}


app.include_router(users.router)
app.include_router(notes.router)

