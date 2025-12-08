from pydantic import BaseModel, Field
from typing import List

class BarCreate(BaseModel):
    name: str = Field(min_length=1)
    city: str = Field(min_length=1)

class Bar(BaseModel):
    id: int
    name: str
    city: str

class BarsResponse(BaseModel):
    items: List[Bar]
