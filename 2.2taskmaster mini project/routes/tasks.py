from fastapi import APIRouter
from schemas.tasks import TaskCreate
from services.tasks_services import create_task_service, get_all_tasks_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(payload: TaskCreate):
    return create_task_service(payload)

@router.get("/")
def get_all_tasks():
    return get_all_tasks_service()
