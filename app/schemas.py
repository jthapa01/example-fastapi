from datetime import datetime
from typing import Optional
import typing
from pydantic import BaseModel, EmailStr



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True



class PostCreate(PostBase):
    pass  # everything from parent



class UserOut(BaseModel):
    id: int
    email:EmailStr
    class Config:
        orm_mode=True

class Post(PostBase):
    # it will let the pydantic to ignore the alchemy model
    id:int
    created_at:datetime
    user_id: int
    user: UserOut
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str]=None

class Vote(BaseModel):
    post_id:int
    dir: typing.Literal[0,1]