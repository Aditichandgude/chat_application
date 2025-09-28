from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app=FastAPI()



@app.get('/one')
def asdf():
    return {"message": "Hello world"}


@app.get('/two')
def hello():
    return{"message":"hii"}


class info(BaseModel):
    username: str
    email: str
    password: str
    dob: date
    

@app.post('/three')
def h():
    return{"message":"How are you"}
