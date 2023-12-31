from pydantic import BaseModel, Field
import datetime


class UserCreate(BaseModel):
    username: str
    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class UserLogin(BaseModel):
    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class LoginRes(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenCreate(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str
    status: bool
    created_date: datetime.datetime


class List(BaseModel):
    page: int
    size: int


class AuthorRes(BaseModel):
    author_name: str
    books: list
