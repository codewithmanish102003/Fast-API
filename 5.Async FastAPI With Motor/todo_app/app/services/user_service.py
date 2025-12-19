from app.core.database import users_collection
from app.utils.security import hash_password, verify_password, create_access_token
from bson import ObjectId

async def register_user(email: str, password: str):
    existing = await users_collection.find_one({"email": email})
    if existing:
        return None

    user = {
        "email": email,
        "password": hash_password(password)
    }

    result = await users_collection.insert_one(user)
    return str(result.inserted_id)

async def login_user(email: str, password: str):
    user = await users_collection.find_one({"email": email})
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    token = create_access_token(
        {"user_id": str(user["_id"]), "email": user["email"]}
    )
    return token
