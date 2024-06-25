from fastapi import FastAPI

from .dependencies import engine
from .dependencies import models
from .routers import items, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"title": "Hello there! Create and View users and items"}