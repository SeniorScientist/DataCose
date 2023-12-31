from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)


class Token(Base):
    __tablename__ = "token"
    user_id = Column(Integer)
    access_token = Column(String(512), primary_key=True)
    refresh_token = Column(String(512), nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String(64), index=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String(128), unique=True, index=True, nullable=False)
    page_number = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    author = relationship("Author", back_populates="books")
