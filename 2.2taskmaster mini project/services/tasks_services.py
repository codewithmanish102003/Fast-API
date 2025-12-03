from schemas.tasks import TaskCreate

# Temporary in-memory DB
fake_tasks_db = []

def create_task_service(payload: TaskCreate):
    task = {
        "id": len(fake_tasks_db) + 1,
        "title": payload.title,
        "description": payload.description,
        "completed": payload.completed
    }
    fake_tasks_db.append(task)
    return task


def get_all_tasks_service():
    return fake_tasks_db
