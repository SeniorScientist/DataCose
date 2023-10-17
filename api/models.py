from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
import datatime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username=Column(String(50), nullable=False)
    email=Column(String(100), unique=True, nullable=False)
    password=Column(String(100), nullable=False)

class Token(Base):
    __table__name = 'token'
    user_id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now) 
    