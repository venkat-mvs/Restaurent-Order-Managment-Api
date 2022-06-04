from pydantic import BaseModel


class Item(BaseModel):
    name: str
    type: str
    cost: float
    isavailable:bool

    class Config:
        orm_mode=True


class Menu(BaseModel):
    items: list[Item] = []