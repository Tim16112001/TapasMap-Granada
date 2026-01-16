from .repository import BarRepository, BarEntity

def create_bar(repo: BarRepository, name: str, city: str) -> BarEntity:
    name = name.strip()
    city = city.strip()
    if not name or not city:
        raise ValueError("Name and city must be non-empty.")
    return repo.add(name, city)

def list_bars(repo: BarRepository) -> list[BarEntity]:
    return repo.list()

def add_bar_rating(repo: BarRepository, bar_id: int, rating: int) -> BarEntity:
    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5")

    bar = repo.add_rating(bar_id, rating)
    if not bar:
        raise KeyError("Bar not found")

    return bar

