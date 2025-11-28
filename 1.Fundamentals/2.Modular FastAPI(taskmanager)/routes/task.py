from fastapi import APIRouter
from schemas.task import Task, TaskResponse
from services.task_services import (
    create_task, get_tasks, get_task_by_id, delete_task
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create(task: Task):
    return create_task(task)

@router.get("/", response_model=list[TaskResponse])
def list_tasks(limit: int = 10):
    return get_tasks(limit)

@router.get("/{task_id}", response_model=TaskResponse)
def get_one(task_id: int):
    return get_task_by_id(task_id)

@router.delete("/{task_id}")
def remove(task_id: int):
    return delete_task(task_id)
