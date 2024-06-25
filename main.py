from fastapi import FastAPI

from dependencies import engine
from dependencies import model

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}