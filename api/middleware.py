from logging import Logger
import random
import time
import string
from fastapi import FastAPI
from starlette.requests import Request

def add_request_logger(app:FastAPI, log:Logger):
    '''
        Request Logger Middeleware
        - logs start and end of a request
    '''


    @app.middleware("http")
    async def RequestLogger(request: Request, call_next):

        idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        log.info(f"rid={idem} path={request.url.path}")
        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = (time.time() - start_time) * 1000
        formatted_process_time = '{0:.2f}'.format(process_time)
        log.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
        
        return response