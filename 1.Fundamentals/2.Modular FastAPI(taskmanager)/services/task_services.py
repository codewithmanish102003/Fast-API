from fastapi import HTTPException
from schemas.task import Task,TaskResponse

tasks_db = []
current_id = 1


def create_task(task: Task) -> TaskResponse:
    global current_id
    new_task = {"id": current_id, **task.dict()}
    tasks_db.append(new_task)
    current_id += 1
    return TaskResponse(**new_task)

def get_tasks(limit: int = 10):
    return [TaskResponse(**task) for task in tasks_db[:limit]]

def get_task_by_id(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return TaskResponse(**task)
    raise HTTPException(404, "Task not found")

def delete_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            tasks_db.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(404, "Task not found")