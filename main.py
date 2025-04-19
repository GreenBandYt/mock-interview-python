# main.py

"""
Главный файл запуска FastAPI-приложения mock-interview-python

Назначение:
- Подключает шаблоны Jinja2
- Подключает статику из папки static/
- Определяет маршрут "/" для гостей
- Рендерит шаблон templates/base/index.html
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Подключение папки static/
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключение папки templates/
templates = Jinja2Templates(directory="templates")

# 📍 Маршрут: /
# 👥 Для: гость
# 📄 Шаблон: templates/base/index.html
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    environment = os.getenv("ENVIRONMENT", "development")
    return templates.TemplateResponse(
        "base/index.html",
        {"request": request, "environment": environment}
    )
