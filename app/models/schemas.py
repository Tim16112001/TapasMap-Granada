from pydantic import BaseModel
from typing import List, Optional

class BarCreate(BaseModel):
    name: str
    city: str

class RatingCreate(BaseModel):
    rating: int

class Bar(BaseModel):
    id: int
    name: str
    city: str
    avg_rating: Optional[float] = None

class BarListResponse(BaseModel):
    items: List[Bar]
