from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import BarCreate, Bar, RatingCreate
from app.services.logic import create_bar, list_bars, add_bar_rating
from app.services.repository import InMemoryBarRepository

router = APIRouter(prefix="/api")

_repo = InMemoryBarRepository()

def get_repo():
    return _repo

@router.post("/bars", response_model=Bar, status_code=201)
def create_bar_route(data: BarCreate, repo=Depends(get_repo)):
    try:
        return create_bar(repo, data.name, data.city)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/bars")
def list_bars_route(repo=Depends(get_repo)):
    return {"items": list_bars(repo)}

@router.post("/bars/{bar_id}/rating", response_model=Bar)
def rate_bar_route(bar_id: int, data: RatingCreate, repo=Depends(get_repo)):
    try:
        return add_bar_rating(repo, bar_id, data.rating)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except KeyError:
        raise HTTPException(status_code=404, detail="Bar not found")
