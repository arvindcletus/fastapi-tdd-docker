"""# project/app/config.py"""


import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Create a class to override the BaseSettings class"""

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", "0")
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    """Create a function to get settings"""
    log.info("Loading config settings from the environment...")
    return Settings()
