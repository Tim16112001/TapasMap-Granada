from .repository import BarRepository, BarEntity

def create_bar(repo: BarRepository, name: str, city: str) -> BarEntity:
    # einfache Geschäftsregel: Name/City getrimmt, nicht leer
    name = name.strip()
    city = city.strip()
    if not name or not city:
        raise ValueError("Name and city must be non-empty.")
    return repo.add(name, city)

def list_bars(repo: BarRepository) -> list[BarEntity]:
    return repo.list()
