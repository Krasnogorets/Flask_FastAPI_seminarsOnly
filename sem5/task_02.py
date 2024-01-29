from hashlib import sha256

import pandas as pd
from fastapi import FastAPI, Request
from typing import Optional, List
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="sem5/templates")
users = []


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: str


# @app.get('/', response_class=HTMLResponse)
# async def index():
#     return "<h1>users</h1>"


@app.get("/", response_class=HTMLResponse)
async def get_all_tasks(request: Request):
    user_table = pd.DataFrame([vars(user) for user in users]).to_html()
    return templates.TemplateResponse("users.html", {'request': request, 'table': user_table})


@app.post("/users/", response_model=User)
async def create_task(user: User):
    user.id = len(users) + 1
    user.name = f"user_{user.id}"
    user.email = f"user_{user.id}@mail.ru"
    user.password = sha256("fjkdfkjdfsjkfdskjf".encode(encoding='utf-8')).hexdigest()
    users.append(user)
    return user


@app.put('/user/{user_id}', response_model=User)
async def update_data(user_id: int, user: User):
    for cur_user in users:
        if user_id == cur_user.id:
            cur_user.name = user.name
            cur_user.email = user.email
            cur_user.password = sha256(user.password.encode(encoding='utf-8')).hexdigest()
            return user


@app.get('/del/{user_id}',response_class=HTMLResponse)
@app.delete('/del/{user_id}', response_class=HTMLResponse)
async def update_data(user_id: int,request: Request):
    for i, cur_user in enumerate(users):
        if user_id == cur_user.id:
            return templates.TemplateResponse("del.html",
                                              {'request': request, 'user': pd.DataFrame([vars(users.pop(i))]).to_html()})

