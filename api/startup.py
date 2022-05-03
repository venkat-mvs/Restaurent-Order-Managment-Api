from logging import Logger
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

''' API level imports '''
import middleware
import utils
from settings import ENV, Env

''' APP level imports '''
from Menu import API as menu

def configure(app:FastAPI, log: Logger, settings:Env = Depends(ENV.values)):
    ''' 
    Configuring API
        - Adding Routers
        - Adding Middelwares
        - Adding Exception handlers
        - Can be used to add other important things
    '''

    @app.on_event("startup")
    async def on_start():

        origins = [
            "*"
        ]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["GET","POST"],
            allow_headers=["*"],
        )
        
        middleware.add_request_logger(app, log=log)

        utils.add_root_redirecter_for(app, to="/docs")

        utils.add_exception_handlers(app, log=log)

        menu_api = menu(log)
        log.info(f"Adding {menu.__name__} Routers... ")
        app.include_router(menu_api)
        log.info(f"Adding {menu.__name__} Routers...done")



    @app.on_event("shutdown")
    async def on_shutdown():
        
        log.info("Server shutdown")


