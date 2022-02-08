"""# project/app/models/tortoise.py"""


from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TextSummary(models.Model):
    """Create a TextSummary model"""

    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        """Function to format the output to string"""
        return self.url


SummarySchema = pydantic_model_creator(TextSummary)
