from fastapi import APIRouter, Depends, Request
from typing import List

from app.models.schemas import BarCreate, Bar
from app.services.logic import create_bar, list_bars
from app.services.repository import BarRepository

# All API endpoints will be under /api/...
router = APIRouter(prefix="/api")


def get_repo(request: Request) -> BarRepository:
    """
    Get the repository instance from app.state.
    This is our single source of truth for bar data.
    """
    return request.app.state.repo


@router.post("/bars", status_code=201, response_model=Bar)
def create_bar_route(
    bar: BarCreate,
    repo: BarRepository = Depends(get_repo),
):
    """
    Create a new tapas bar.
    """
    created = create_bar(repo, bar.name, bar.city)
    return created


from typing import List, Dict

@router.get("/bars")
def list_bars_route(
    repo: BarRepository = Depends(get_repo),
) -> Dict[str, List[Bar]]:
    """
    List all tapas bars.
    Returns a JSON object with an "items" list.
    """
    items: List[Bar] = list_bars(repo)
    return {"items": items}

