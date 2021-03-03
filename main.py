from fastapi import FastAPI 
from pydantic import BaseModel

app=FastAPI()

libdb=[]

class myInfo(BaseModel):
    name: str
    srn: str
    fun_fact: str



class Book(BaseModel):
    bookname: str
    bookid: int
    price: float
    
    
@app.get("/")
def basic():
    return{"greetings":"Welcome to PESU Digital Library"}

@app.get("/genre")
def get_genre():
    return libdb

@app.get("/genre/{book_id}")
def get_a_book(book_id: int):
    book=book_id-1
    return libdb[book]

@app.post("/genre")
def add_book(book:Book):
    libdb.append(book.dict())
    return libdb[-1]

@app.delete("/genre/{book_id}")
def delete_book(book_id:int):
    libdb.pop(book_id-1)
    return{"task":"deletion successful"}

@app.get("/myinfo")
def my_info():
    info={
        "name":"Ananya Bhatnagar",
        "srn":"PES2UG19CS038",
        "fun_fact":"I can crack my left ring finger bone"
    }
    return info