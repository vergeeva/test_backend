from datetime import datetime
import uuid
from typing import List
from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    click_count: int

    class Config:
        orm_mode = True


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    first_click_date: datetime


class ListUserResponse(BaseModel):
    users: List[UserResponse]
