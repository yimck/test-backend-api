from fastapi import FastAPI
from pydantic import BaseModel
# from db import insert

app = FastAPI()

class Item(BaseModel):
    name: str
    ingredients: str
    price: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_items():
    return {"World": "Hello"}


@app.post("/items")
def create_item(item_id: str, item: Item):
    temp_tuple = item.name, item.ingredients, item.price
    # insert(temp_tuple)
    return {"item": temp_tuple}

@app.put("/items/{item_id}")
def update_item(item_id: str):
    return
