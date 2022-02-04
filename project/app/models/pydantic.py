"""# project/app/models/pydantic.py"""


from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    """Create a summary payload schema"""
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    """Create a summary response schema"""
    id: int
