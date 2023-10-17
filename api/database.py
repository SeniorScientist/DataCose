from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Replace the SQLite connection URL with your PostgreSQL connection URL
url = URL.create(
    drivername="postgresql",
    username="postgre",
    password="123",
    host="localhost",
    database="datacose",
    port=5432
)

#Create a PostgreSQL engine instance
engine = create_engine(url)

#Create declarative base meta instance
Base = declarative_base()

#Create session local class for session maker
Session = sessionmaker(bind=engine, expire_on_commit=False)
session = Session()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)
