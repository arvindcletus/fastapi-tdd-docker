"""# project/app/api/crud.py"""


from typing import List

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """Function that creates a summary"""
    summary = TextSummary(url=payload.url, summary="")
    await summary.save()
    return summary.id


async def get(id: int) -> dict | None:
    """Function that fetches a single summary"""
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> List:
    """Function that fetches all summary"""
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    """Function to delete a summary by id"""
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> dict | None:
    """Function to update a summary by id"""
    summary = await TextSummary.filter(id=id).update(url=payload.url, summary=payload.summary)
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary
    return None
