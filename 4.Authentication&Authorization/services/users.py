from typing import Optional

from core.database import connect
from pymongo.collection import Collection
from schemas.users import UserCreate, UserInDB
from utils.security import create_access_token, hash_password, verify_password


def get_users_collection() -> Collection:
    db = connect()
    return db.get_collection("users")


def create_user(user: UserCreate) -> dict:
    users = get_users_collection()
    if users.find_one({"email": user.email}):
        raise ValueError("Email already registered")
    hashed = hash_password(user.password)
    doc = {"email": user.email, "hashed_password": hashed, "full_name": user.full_name, "role": user.role}
    res = users.insert_one(doc)
    created_user = users.find_one({"_id": res.inserted_id})
    created_user["_id"] = str(created_user["_id"])
    return created_user


def authenticate_user(email: str, password: str) -> Optional[dict]:
    users = get_users_collection()
    u = users.find_one({"email": email})
    if not u:
        return None
    if not verify_password(password, u.get("hashed_password")):
        return None
    u["_id"] = str(u["_id"])
    return u


def create_tokens_for_user(user: dict) -> dict:
    access = create_access_token(str(user.get("_id")), user.get("role"))
    return {"access_token": access, "token_type": "bearer"}
