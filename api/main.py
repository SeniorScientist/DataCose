from sqlalchemy import func, select
import schemas
import models
from jose import jwt
from models import User, Token
from fastapi import FastAPI, Depends, HTTPException, status
from auth_bearer import JWTBearer
from database import Base, engine, SessionLocal
from sqlalchemy.orm import session
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, add_pagination, paginate

from utils import (
    ALGORITHM,
    JWT_SECRET_KEY,
    create_access_token,
    create_refresh_token,
    verify_password,
    get_hashed_password,
)

origins = ["http://127.0.0.1:3000", "http://localhost:3000"]

app = FastAPI()
add_pagination(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_count(q):
    count_q = q.statement.order_by(None)
    count = q.session.execute(count_q).scalar()
    return count


@app.get("/")
def read_root() -> str:
    return {"Hello World"}


@app.post("/auth/register")
def register_user(user: schemas.UserCreate, session: session = Depends(get_session)) -> str:
    existing_user = session.query(models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_hashed_password(user.password)

    new_user = models.User(username=user.username, email=user.email, password=encrypted_password)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"user created successfully"}


@app.post("/auth/login")
def login(request: schemas.UserLogin, db: session = Depends(get_session)) -> schemas.LoginRes:
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    access = create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = models.Token(user_id=user.id, access_token=access, refresh_token=refresh, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {"access_token": access, "refresh_token": refresh, "token_type": "bearer"}


## updating...
@app.get("/auth/refresh")
def refresh(dependencies=Depends(JWTBearer()), db: session = Depends(get_session)):
    token = dependencies
    payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
    user_id = payload["sub"]
    token_record = db.query(models.Token).all()
    info = []
    for record in token_record:
        print("record", record)
        if (datetime.utcnow() - record.created_date).days > 1:
            info.append(record.user_id)
    if info:
        existing_token = db.query(models.Token).where(Token.user_id.in_(info)).delete()
        db.commit()

    existing_token = (
        db.query(models.Token).filter(models.Token.user_id == user_id, models.Token.access_token == token).first()
    )
    if existing_token:
        existing_token.status = False
        db.add(existing_token)
        db.commit()
        db.refresh(existing_token)

    access = create_access_token(user_id)

    return {"access_token": access}


@app.post("/auth/logout")
def logout(dependencies=Depends(JWTBearer()), db: session = Depends(get_session)):
    token = dependencies
    payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
    user_id = payload["sub"]
    token_record = db.query(models.Token).all()
    info = []
    for record in token_record:
        print("record", record)
        if (datetime.utcnow() - record.created_date).days > 1:
            info.append(record.user_id)
    if info:
        existing_token = db.query(models.Token).where(Token.user_id.in_(info)).delete()
        db.commit()

    existing_token = (
        db.query(models.Token).filter(models.Token.user_id == user_id, models.Token.access_token == token).first()
    )
    if existing_token:
        existing_token.status = False
        db.add(existing_token)
        db.commit()
        db.refresh(existing_token)
    return {"Logout Successfully"}


# @app.get("/authors")
# async def read_authors(
#     db: session = Depends(get_session),
# ) -> Page[schemas.AuthorRes]:
#     return paginate(db, select(models.Author))


@app.get("/books")
async def read_books(request: schemas.List, dependencies=Depends(JWTBearer()), db: session = Depends(get_session)):
    return (
        db.query(models.Book)
        .offset(request.page_number * request.page_count)
        .limit((request.page_number + 1) * request.page_count)
        .all()
    )
