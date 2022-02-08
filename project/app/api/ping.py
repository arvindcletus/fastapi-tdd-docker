"""# project/app/api/ping.py"""


from app.config import Settings, get_settings
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """Function that gets a ping"""
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
