from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional

class StandardResponse(BaseModel):
    message: str = ""
    data: Optional[list] = None
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

    @validator('name')
    def validate_name_length(cls, v):
        if len(v) < 3 or len(v) > 50:
            raise ValueError('Name must be between 3 and 50 characters')
        return v

    # For the number validator, you can add an example validator like this:
    @validator('password')
    def validate_password_length(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v

