from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Replace the SQLite connection URL with your PostgreSQL connection URL
url = URL.create(
    drivername="postgresql", username="postgres", password="postgres", host="localhost", database="postgres", port=5432
)

# Create a PostgreSQL engine instance
engine = create_engine(url)

print("DB Linked...")

# Create declarative base meta instance
Base = declarative_base()

# Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
