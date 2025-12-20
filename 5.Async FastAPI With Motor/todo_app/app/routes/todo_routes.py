from fastapi import APIRouter, Depends, HTTPException
from app.schemas.todo_schema import TodoCreate, TodoUpdate
from app.dependencies.auth import get_current_user
from app.services.todo_service import (
    create_todo, get_todos, update_todo, delete_todo
)

router = APIRouter(
    prefix="/api/todos",
    tags=["Todos"]
)

@router.post("/")
async def create(
    data: TodoCreate,
    user=Depends(get_current_user)
):
    todo_id = await create_todo(user["id"], data.dict())
    return {"id": todo_id}


@router.get("/")
async def list_todos(user=Depends(get_current_user)):
    return await get_todos(user["id"])


@router.put("/{todo_id}")
async def update(
    todo_id: str,
    data: TodoUpdate,
    user=Depends(get_current_user)
):
    updated = await update_todo(todo_id, user["id"], data.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@router.delete("/{todo_id}")
async def delete(
    todo_id: str,
    user=Depends(get_current_user)
):
    deleted = await delete_todo(todo_id, user["id"])
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}
