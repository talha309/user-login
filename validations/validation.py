from pydantic import BaseModel, Field, validator
from typing import Optional, List, Any

class StandardResponse(BaseModel):
    message: str = ""
    data: Optional[List[Any]] = None
    status: str = ""

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None  # type: ignore
    completed: bool = False

class LoginUser(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r'^\S+@\S+$')
    password: str = Field(..., min_length=6)

    @validator('password')
    def validate_password_length(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v
