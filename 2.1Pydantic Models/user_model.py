from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List


class User(BaseModel):
    """
    User model with comprehensive validation:
    - name: 3-40 characters
    - age: between 18 and 55
    - city: auto-strip spaces
    - skills: list of strings, minimum 1 skill
    - username: custom validator - no spaces allowed
    """
    
    model_config = ConfigDict(str_strip_whitespace=True)
    
    name: str = Field(..., min_length=3, max_length=40, description="User's full name (3-40 characters)")
    age: int = Field(..., ge=18, le=55, description="User's age (18-55)")
    city: str = Field(..., description="User's city (spaces auto-stripped)")
    skills: List[str] = Field(..., min_length=1, description="List of skills (minimum 1 required)")
    username: str = Field(..., description="Username (no spaces allowed)")
    
    @field_validator('username')
    @classmethod
    def validate_username_no_spaces(cls, v: str) -> str:
        """Custom validator to ensure username has no spaces"""
        if ' ' in v:
            raise ValueError('Username cannot contain spaces')
        return v
    
    @field_validator('city')
    @classmethod
    def strip_city_spaces(cls, v: str) -> str:
        """Auto-strip leading and trailing spaces from city"""
        return v.strip()
    
    @field_validator('skills')
    @classmethod
    def validate_skills_not_empty(cls, v: List[str]) -> List[str]:
        """Ensure skills list is not empty and contains valid strings"""
        if not v:
            raise ValueError('At least one skill is required')
        # Strip whitespace from each skill
        return [skill.strip() for skill in v if skill.strip()]


class UserResponse(BaseModel):
    """Response model for User"""
    name: str
    age: int
    city: str
    skills: List[str]
    username: str
    message: str = "User created successfully"
