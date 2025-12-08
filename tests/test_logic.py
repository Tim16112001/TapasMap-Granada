from app.services.logic import create_bar, list_bars
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
