from app.services.logic import create_bar, list_bars, add_bar_rating
from app.services.repository import InMemoryBarRepository

def test_create_and_list_bars():
    repo = InMemoryBarRepository()
    bar = create_bar(repo, "Bar Granada", "Granada")
    assert bar.id == 1
    assert bar.name == "Bar Granada"
    assert len(list_bars(repo)) == 1

def test_create_bar_rejects_empty():
    repo = InMemoryBarRepository()
    try:
        create_bar(repo, " ", " ")
        assert False, "expected ValueError"
    except ValueError:
        assert True

def test_add_rating():
    repo = InMemoryBarRepository()
    bar = create_bar(repo, "Bar Test", "Granada")

    add_bar_rating(repo, bar.id, 5)
    add_bar_rating(repo, bar.id, 3)

    updated = repo.get(bar.id)
    assert updated.avg_rating == 4.0
