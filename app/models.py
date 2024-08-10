from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email =Column(String)
    hashed_password = Column(String)

    projects = relationship("Project", back_populates="owner")
    blogs = relationship("Blog", back_populates="owner")

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    project_link = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="projects")

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="blogs")

class ContactInfo(Base):
    __tablename__ = 'contact_infos'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    github =Column(String)
    phone = Column(String)
