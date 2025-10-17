from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    done: bool = False

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
