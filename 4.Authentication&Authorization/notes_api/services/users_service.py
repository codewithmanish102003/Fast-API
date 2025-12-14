from fastapi import HTTPException, status
from core.database import users_collection
from utils.security import hash_password, verify_password, create_access_token

def register_user(payload):
    if users_collection.find_one({"email": payload.email}):
        raise HTTPException(409, "User already exists")

    user = {
        "email": payload.email,
        "hashed_password": hash_password(payload.password),
        "role": "user"
    }
    users_collection.insert_one(user)

    return {"message": "User registered"}

def login_user(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

    return create_access_token({
        "sub": user["email"],
        "role": user["role"],
        "user_id": str(user["_id"])
    })
