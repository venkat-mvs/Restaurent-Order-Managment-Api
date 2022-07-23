from logging import Logger
from fastapi import Depends
from fastapi.routing import APIRoute, APIRouter
from sqlalchemy.orm import Session

from API.db import crud, utils, schemas

def API(log: Logger) -> APIRoute:
    router = APIRouter(
        prefix = "/menu",
        tags = ["Menu"]
    )

    @router.get("/")
    async def get_menu(db:Session = Depends(utils.get_db)):
        return crud.get_menu(db)

    
    @router.post("/")
    async def add_item(item: schemas.Item ,db:Session = Depends(utils.get_db)):
        
        item = crud.add_item(db, item=item)

        return item
    
    return router