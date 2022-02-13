"""# project/app/models/pydantic.py"""


from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    """Create a summary payload schema"""

    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    """Create a summary response schema"""

    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    """Create a summary update schema"""

    summary: str
