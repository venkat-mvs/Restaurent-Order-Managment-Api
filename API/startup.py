from logging import Logger
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

''' API level imports '''
import API.middleware as middleware
import API.utils as utils
from API.settings import ENV, Env

''' APP level imports '''
from API.menu.router import API as menu
from API.biller.routers import API as biller
from API.order_placement.routers import API as order
from API.table.routers import API as tables
from API.customer.router import API as customer

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

        menu_routes = menu(log)
        biller_routes = biller(log)
        order_routes = order(log)
        table_routes = tables(log)
        customer_routes = customer(log)

        app.include_router(menu_routes)
        app.include_router(biller_routes)
        app.include_router(order_routes)
        app.include_router(table_routes)
        app.include_router(customer_routes)
        log.info(f"Adding Routers...done")



    @app.on_event("shutdown")
    async def on_shutdown():
        
        log.info("Server shutdown")


