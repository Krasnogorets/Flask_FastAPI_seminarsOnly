import random
from datetime import date
from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, validator
from sqlalchemy import create_engine
from hashlib import sha256
from datetime import datetime as dt

from starlette.responses import HTMLResponse

app = FastAPI()
DATABASE_URL = "sqlite:///new1.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table("users", metadata, sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("second_name", sqlalchemy.String(60)),
                         sqlalchemy.Column("birthday", sqlalchemy.DATE),
                         sqlalchemy.Column("email", sqlalchemy.String(60)),
                         sqlalchemy.Column("address", sqlalchemy.String(120)))

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class UserIn(BaseModel):
    name: str = Field(max_length=32, min_length=2)
    second_name: str = Field(max_length=60, min_length=2)
    birthday: date
    # = Field(
    #     regex="^(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|"
    #           "(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))"
    #           "(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:0?2(\/|-|\.)29\3"
    #           "(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579]"
    #           "[26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:"
    #           "(?:0?[1-9])|(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4"
    #           "(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
    email: EmailStr = Field(max_length=60)
    address: str = Field(max_length=120, min_length=5)


# SELECT strftime('%d.%m.%Y', '2021-12-01');
class User(BaseModel):
    id: int
    name: str = Field(max_length=32, min_length=2)
    second_name: str = Field(max_length=60, min_length=2)
    birthday: date
    email: EmailStr = Field(max_length=60)
    address: str = Field(max_length=120, min_length=5)


@app.get('/', response_class=HTMLResponse)
async def index():
    return '<h1>start</h1>'


# @app.get("/fake_users/{count}")
# async def create_users(count: int):
#     for i in range(count):
#         bd = dt.strptime('1.11.1900', '%d.%m.%Y')
#         query = users.insert().values(name=f'{i}', second_name=f'user_user_{i}', email=f'user_{i}@mail.ru',
#                                       birthday=bd, address=f'Moscow, Street,{random.randint(2, 45)} '
#                                                            f'buld., flat{random.randint(1, 200)}')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


@app.post("/users/", response_model=UserIn)
async def create_user(user: User):
    query = users.insert().values(name=user.name, second_name=user.second_name, email=user.email,
                                  birthday=user.birthday, address=user.address)
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
    query = users.update().where(users.c.id == user_id).values(name=new_user.name, second_name=new_user.second_name,
                                                               email=new_user.email, birthday=new_user.birthday,
                                                               address=new_user.address)
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User id={user_id} deleted'}
