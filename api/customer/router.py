from logging import Logger
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from API.db import crud, schemas, utils


def API(logger: Logger):

    router = APIRouter(
        prefix = "/customer",
        tags = ["Customer"]
    )

    @router.post("/")
    def add_new_customer(customer:schemas.Customer,db:Session= Depends(utils.get_db)):
        customer = crud.add_customer(db, customer)
        return customer


    return router
