# FastAPI Auth + JWT + Roles (PyMongo)

This is a minimal example showing user authentication with JWT and roles using FastAPI and PyMongo.

Quick start:

1. Copy `.env.sample` to `.env` and fill `SECRET_KEY` and `ADMIN_SECRET`.
2. Start MongoDB locally and run:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API highlights:
- `POST /users/register` — create a user
- `POST /users/token` — get an access token (form-data: username, password)
- `GET /users/me` — get current user
- `POST /notes/` — create note (needs auth)
