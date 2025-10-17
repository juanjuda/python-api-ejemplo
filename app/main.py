from fastapi import FastAPI, HTTPException
from app.models import Item, ItemCreate
from typing import List

app = FastAPI(title="Tasks API", version="1.0.0")

items_db: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de tareas!"}

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.post("/items", response_model=Item)
def create_item(new_item: ItemCreate):
    item = Item(id=len(items_db)+1, **new_item.dict())
    items_db.append(item)
    return item

@app.patch("/items/{item_id}/done", response_model=Item)
def mark_item_done(item_id: int):
    for item in items_db:
        if item.id == item_id:
            item.done = True
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")
