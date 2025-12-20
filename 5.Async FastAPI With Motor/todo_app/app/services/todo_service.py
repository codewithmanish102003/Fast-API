from app.core.database import todos_collection
from bson import ObjectId
from datetime import datetime

async def create_todo(user_id: str, data: dict):
    todo = {
        "title": data["title"],
        "description": data.get("description"),
        "completed": False,
        "owner_id": user_id,
        "created_at": datetime.utcnow()
    }
    result = await todos_collection.insert_one(todo)
    return str(result.inserted_id)


async def get_todos(user_id: str):
    todos = []
    cursor = todos_collection.find({"owner_id": user_id})

    async for doc in cursor:
        todos.append({
            "id": str(doc["_id"]),
            "title": doc["title"],
            "description": doc.get("description"),
            "completed": doc["completed"]
        })

    return todos


async def update_todo(todo_id: str, user_id: str, data: dict):
    result = await todos_collection.find_one_and_update(
        {"_id": ObjectId(todo_id), "owner_id": user_id},
        {"$set": data},
        return_document=True
    )

    if not result:
        return None

    result["id"] = str(result["_id"])
    del result["_id"]
    return result


async def delete_todo(todo_id: str, user_id: str):
    result = await todos_collection.find_one_and_delete(
        {"_id": ObjectId(todo_id), "owner_id": user_id}
    )
    return result is not None
