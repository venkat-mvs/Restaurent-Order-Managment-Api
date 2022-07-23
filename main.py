''' Framework Level Modules '''
from sys import prefix
from fastapi import FastAPI, logger as fastapi_logger
import uvicorn

''' API level modules '''
from API.logger import logger,logging 
import API.startup as startup
from API.settings import ENV, Env
from API.db import models
from API.db.db import engine



def main(settings:Env):
    ''' App Initialization and Configuration '''
    
    app = FastAPI(
                title= settings.API_TITLE,
                version=settings.API_VERSION,
                docs_url="/swagger",
                redoc_url="/docs",
                prefix="/api"
        ) 
    
    logger.setLevel(logging.DEBUG)

    logger.info("Ensuring DB tables")
    models.Base.metadata.create_all(bind=engine)
    logger.info("Ensuring DB tables...done")

    #print(logging.root.manager.loggerDict)
    
    logger.info("Configuring Server...")
        
    startup.configure(app, log = logger, settings=settings)
    
    logger.info("Configuring Server...done")
    
    return app

app = main(ENV.values())

if __name__ == '__main__':
    ''' Web Server init '''

    settings = ENV.values()

    logger.info(f"Starting Server at http://{settings.HOST}:{settings.PORT}")

    uvicorn.run("main:app",
                host = settings.HOST,
                port = settings.PORT,
                reload = True,
                use_colors = True,
                reload_includes= ["*"],
                server_header = True,
                log_level = logging.ERROR
    ) 