# project/app/main.py

import uvicorn
from fastapi import FastAPI, Depends

from .config import get_settings, Settings

app = FastAPI()


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
