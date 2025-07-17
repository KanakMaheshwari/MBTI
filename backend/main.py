from typing import Union
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from utils import *

app = FastAPI()

class QuestionAndAnswers(BaseModel):
    id:int
    answer:int

class Quiz(BaseModel):
    quiz: List[QuestionAndAnswers]





@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/quiz")
def get_qa():
    return reading_json()


@app.post("/submit")
def submit_ans(answer:Quiz):
    return {"submitted":"number"}



