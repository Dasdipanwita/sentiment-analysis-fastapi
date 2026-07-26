from pydantic import BaseModel, Field


class Review(BaseModel):
    text: str = Field(min_length=1)