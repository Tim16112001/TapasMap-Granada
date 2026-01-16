from typing import Protocol, List, Optional, Dict

class BarEntity:
    def __init__(self, id: int, name: str, city: str):
        self.id = id
        self.name = name
        self.city = city
        self.ratings_sum = 0
        self.ratings_count = 0
        self.avg_rating = None

class BarRepository(Protocol):
    def add(self, name: str, city: str) -> BarEntity: ...
    def list(self) -> List[BarEntity]: ...
    def get(self, id: int) -> Optional[BarEntity]: ...
    def add_rating(self, bar_id: int, rating: int) -> Optional[BarEntity]: ...

class InMemoryBarRepository:
    def __init__(self):
        self._data: Dict[int, BarEntity] = {}
        self._next_id = 1

    def add(self, name: str, city: str) -> BarEntity:
        bar = BarEntity(self._next_id, name, city)
        self._data[self._next_id] = bar
        self._next_id += 1
        return bar

    def list(self) -> List[BarEntity]:
        return list(self._data.values())

    def get(self, id: int) -> Optional[BarEntity]:
        return self._data.get(id)

    def add_rating(self, bar_id: int, rating: int) -> Optional[BarEntity]:
        bar = self._data.get(bar_id)
        if not bar:
            return None

        bar.ratings_sum += rating
        bar.ratings_count += 1
        bar.avg_rating = round(bar.ratings_sum / bar.ratings_count, 2)
        return bar


