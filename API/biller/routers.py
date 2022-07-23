from logging import Logger
from fastapi import Depends
from fastapi.params import Query
from fastapi.routing import APIRoute, APIRouter

from API.biller.service import BillingService

def API(log: Logger) -> APIRoute:
    router = APIRouter(
        prefix = "/bill",
        tags = ["Bill"]
    )

    @router.get("/{tableid:int}")
    async def get_menu(tableid:int):
        return BillingService().get_bill(table_id=tableid)
    
    return router