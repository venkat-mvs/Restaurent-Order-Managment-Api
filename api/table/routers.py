from logging import Logger
from sqlalchemy.orm import Session
import fastapi

from API.db import crud, utils, schemas

def API(logger: Logger):

    router = fastapi.APIRouter(
        prefix = "/tables",
        tags = ["Table"]
    )

    @router.get("/")
    def fetch_tables(db:Session = fastapi.Depends(utils.get_db)):
        return crud.get_tables(db)

    @router.post("/")
    def add_table_entry(table_entry: schemas.Table, 
                        db: Session = fastapi.Depends(utils.get_db)):

        return crud.add_table(db, table_entry)

    return router
