from typing import List, Optional
from pydantic import BaseModel, EmailStr


# User Schemas
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: EmailStr
    password: str
    confirm_password:str



class User(UserBase):
    id: int
    projects: List['Project'] = []
    blogs: List['Blog'] = []

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreateResponse(BaseModel):
    message: str
    user: ShowUser


# Authentication Schemas
class Login(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Project Schemas
class ProjectBase(BaseModel):
    title: str
    description: str
    project_link: str


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Blog Schemas
class BlogBase(BaseModel):
    title: str
    body: str


class BlogCreate(BlogBase):
    pass


class Blog(BlogBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: User

    class Config:
        orm_mode = True


# Contact Information Schemas
class ContactInfoBase(BaseModel):
    name: str
    email: str
    github: Optional[str] = None
    phone: Optional[str] = None


class ContactInfoCreate(ContactInfoBase):
    pass


class ContactInfo(ContactInfoBase):
    id: int

    class Config:
        orm_mode = True
