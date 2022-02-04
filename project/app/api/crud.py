"""# project/app/api/crud.py"""


from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """Test that a summary is created"""
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> dict | None:
    """Test that a single summary can be fetched"""
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None
