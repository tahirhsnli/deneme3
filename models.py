from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
Base = declarative_base()

from settings import settings
engine = create_engine(settings.DATABASE_URL)

class User(Base):

    __tablename__ = 'users'

    user_id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

class UserCreate(BaseModel):
    name: str
    surname : str
    age : int
    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    user_id : int
    name : Optional[str]
    surname : Optional[str]
    age : Optional[int]
    class Config:
        orm_mode = True