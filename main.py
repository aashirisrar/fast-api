from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .configurations.database import engine
from . import models
from .routers import item, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(item.router)

@app.get("/")
def read_root():
    return {"title": "Hello there! Create and View users and items"}