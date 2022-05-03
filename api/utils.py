from http.client import HTTPException
from fastapi import FastAPI, Request
from logging import Logger
from fastapi.responses import RedirectResponse, JSONResponse

def add_root_redirecter_for(app: FastAPI, to:str):
    
    @app.get("/",include_in_schema=False)
    async def redirect():
        return RedirectResponse(to)

def add_exception_handlers(app: FastAPI, log: Logger):

    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc_details: Exception):

        if exc_details.__class__ in [ValueError]:
            return JSONResponse(
                status_code=400,
                content = {
                    "message": str(exc_details)
                }
            )
        else:
            log.exception(exc_details)
            return JSONResponse(
                status_code=500,
                content = {
                    "error":str(exc_details)
                }
            )
