from logging import Logger
from fastapi import Depends
from fastapi.routing import APIRoute, APIRouter
from sqlalchemy.orm import Session

from API.db import crud, models, utils, schemas


def API(log: Logger) -> APIRoute:
    router = APIRouter(
        prefix = "/order",
        tags = ["Order"]
    )

    @router.post("/")
    async def add_order(order:schemas.OrderEntry, db:Session = Depends(utils.get_db)):
        return crud.add_table_order(db, order)

    @router.get("/quantity/item/{item_id:int}/table/{table_id:int}")
    async def get_order(table_id: int, item_id:int, db:Session = Depends(utils.get_db)):
        return crud.get_order(db, schemas.OrderEntry(table_id=table_id, item_id=item_id, quantity_ordered=0))

    # @router.get('/{table:int}')
    # async def get_orders(table:int, db:Session = Depends(utils.get_db)):
    #     return [mapper(obj['Orders']) for obj in crud.get_table_items_ordered_by_table_id(db, table_id=table)]

    
    return router