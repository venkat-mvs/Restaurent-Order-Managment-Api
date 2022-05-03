from logging import Logger
from fastapi.routing import APIRoute, APIRouter


def API(log: Logger) -> APIRoute:
    router = APIRouter(
        prefix = "/menu",
        tags = ["Menu"]
    )

    @router.get("/")
    def get_menu():
        return {
            "item": {
                "id": 1,
                "name": "Pizza",
                "quantity": 2,
                "cost": 30
            }
        }
    
    return router