from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    type: str
    cost: float
    isavailable:bool

    class Config:
        orm_mode=True


class Menu(BaseModel):
    items: list[Item] = []

class Table(BaseModel):
    seats: int
    isoccupied: bool

    class Config:
        orm_mode = True

class Customer(BaseModel):
    phone_number: str = Field(regex=r"((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}")

    class Config:
        orm_mode = True

class OrderEntry(BaseModel):
    table_id: int 
    item_id: int
    quantity_ordered: int

    class Config:
        orm_mode = True

class BillItem(BaseModel):
    name: str
    cost: float
    count: int

    class Config:
        orm_mode = True

class Bill(BaseModel):
    items: list[BillItem]
    cost: float

