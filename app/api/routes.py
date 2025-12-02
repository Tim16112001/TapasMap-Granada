from fastapi import APIRouter, Depends, HTTPException, Request
from ..models.schemas import BarCreate, Bar, BarsResponse
from ..services.repository import BarRepository
from ..services.logic import create_bar, list_bars

router = APIRouter()

def get_repo(request: Request) -> BarRepository:
    return request.app.state.repo

@router.post("/bars", response_model=Bar, status_code=201)
def create_bar_endpoint(payload: BarCreate, repo: BarRepository = Depends(get_repo)):
    try:
        entity = create_bar(repo, payload.name, payload.city)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return Bar(id=entity.id, name=entity.name, city=entity.city)

@router.get("/bars", response_model=BarsResponse)
def list_bars_endpoint(repo: BarRepository = Depends(get_repo)):
    items = [Bar(id=b.id, name=b.name, city=b.city) for b in list_bars(repo)]
    return BarsResponse(items=items)

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}
