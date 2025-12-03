from fastapi import FastAPI, HTTPException
from user_model import User, UserResponse
from typing import List

app = FastAPI(
    title="User Validation API",
    description="FastAPI application to test User model with comprehensive validation",
    version="1.0.0"
)

# In-memory storage for demonstration
users_db: List[User] = []


@app.get("/")
def home():
    """Root endpoint"""
    return {
        "message": "User Validation API",
        "endpoints": {
            "POST /users": "Create a new user",
            "GET /users": "Get all users",
            "GET /users/{username}": "Get user by username"
        }
    }


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: User):
    """
    Create a new user with validation:
    - name: 3-40 characters
    - age: 18-55
    - city: auto-stripped spaces
    - skills: minimum 1 skill
    - username: no spaces allowed
    """
    # Check if username already exists
    if any(u.username == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    users_db.append(user)
    
    return UserResponse(
        name=user.name,
        age=user.age,
        city=user.city,
        skills=user.skills,
        username=user.username,
        message="User created successfully"
    )


@app.get("/users", response_model=List[User])
def get_all_users():
    """Get all users"""
    return users_db


@app.get("/users/{username}", response_model=User)
def get_user_by_username(username: str):
    """Get a specific user by username"""
    for user in users_db:
        if user.username == username:
            return user
    
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{username}")
def delete_user(username: str):
    """Delete a user by username"""
    global users_db
    initial_length = len(users_db)
    users_db = [u for u in users_db if u.username != username]
    
    if len(users_db) == initial_length:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": f"User '{username}' deleted successfully"}
