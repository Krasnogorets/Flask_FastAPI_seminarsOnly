"""
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""
import random
from hashlib import sha256

import uvicorn as uvicorn
from fastapi import FastAPI
from typing import Optional, List
from fastapi.responses import HTMLResponse

from pydantic import BaseModel
from fastapi.responses import RedirectResponse, JSONResponse
import pandas as pd

app = FastAPI()

tasks = []


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: bool


tasks.append(Task(id=1, title='first', status=True))


# print(*tasks)

@app.get("/")
async def root():
    return {"item_id": None, "item": None}
    # return RedirectResponse("https://www.theyachtmarket.com/en/brokers/")


@app.get("/tasks/", response_class=HTMLResponse)
async def get_all_tasks():
    task_table = pd.DataFrame([vars(task) for task in tasks]).to_html()
    return task_table


@app.post("/new/", response_model=Task)
async def create_task(task: Task):
    id = len(tasks) + 1
    task.id = id
    task.title = f"task_{id}"
    task.description = sha256("fjkdfkjdfsjkfdskjf".encode(encoding='utf-8')).hexdigest()
    task.status = True
    tasks.append(task)
    print(*tasks)
    return task


@app.get("/done")
async def done():
    return "<h1>new task added</h1>"

# if __name__ == "__main__":
#     uvicorn.run("sem5.task_01:app", host='127.0.0.1', port=8888, reload=True)
