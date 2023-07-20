from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    """
    This looks almost same but earlier we were sending
    other fields too like the created and the id of the post
    but now they will not be included
    """
    title: str
    # created_at: datetime
    user_id:int
    votes:int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr
    password : str
    username : str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id : int
    dir: int = Field(..., ge=0, le=1)