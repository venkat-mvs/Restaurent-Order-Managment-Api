from pydantic import BaseSettings
from functools import lru_cache

class Env(BaseSettings):

    HOST: str = "localhost" 
    PORT: int = 8000
    API_TITLE: str 
    API_VERSION: str
    SQL_CONNECTION_STRING: str

    class Config:
        env_file = ".env"

class ENV:
    @lru_cache
    def values() -> Env:
        return Env()
