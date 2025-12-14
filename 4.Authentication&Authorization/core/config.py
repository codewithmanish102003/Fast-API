from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Auth + JWT + Roles"
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_db: str = "fastapi_auth"
    secret_key: str = "CHANGE_ME_TO_SOMETHING_RANDOM"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    admin_secret: str = "CHANGE_ME_ADMIN_SECRET"

    model_config = {"env_file": ".env"}


settings = Settings()

