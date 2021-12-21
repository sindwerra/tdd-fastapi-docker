# project/app/main.py

import os

import uvicorn
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from .config import get_settings, Settings

app = FastAPI()


register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=False,
    add_exception_handlers=True,
)


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }


@app.get('/favicon.ico')
def ignore_err():
    return 'Just ignore 404 favicon'


@app.get('/')
def index():
    return '0 error, 0 warning'


if __file__ == '__main__':
    uvicorn.run(app)
