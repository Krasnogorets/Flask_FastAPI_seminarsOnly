from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import create_engine
from hashlib import sha256
from fastapi.responses import HTMLResponse

app = FastAPI()
DATABASE_URL = "sqlite:///new.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table("users", metadata, sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(64)))

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=64)


# @app.get("/fake_users/{count}")
# async def create_users(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user_{i}', email=f'user_{i}@mail.ru',
#                                       password=sha256(f'user_{i}'.encode(encoding='utf-8')).hexdigest())
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}

@app.get('/',response_class=HTMLResponse)
async def index():
    return '<h1>start</h1>'



@app.post("/users/", response_model=UserIn)
async def create_user(user: User):
    query = users.insert().values(name=user.name, email=user.email,
                                  password=sha256(user.password.encode(encoding='utf-8')).hexdigest())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.get("/users/", response_model=List[UserIn])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=UserIn)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: User):
    query = users.update().where(users.c.id == user_id).values(name=new_user.name, email=new_user.email,
                                                               password=sha256(new_user.password.encode(
                                                                   encoding='utf-8')).hexdigest())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User id={user_id } deleted'}

