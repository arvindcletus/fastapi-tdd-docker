"""# project/app/api/crud.py"""


from typing import List
from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """Function that creates a summary"""
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
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
