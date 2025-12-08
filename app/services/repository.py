from typing import Protocol, List, Optional, Dict

class BarEntity:
    def __init__(self, id: int, name: str, city: str):
        self.id = id
        self.name = name
        self.city = city

class BarRepository(Protocol):
    def add(self, name: str, city: str) -> BarEntity: ...
    def list(self) -> List[BarEntity]: ...
    def get(self, id: int) -> Optional[BarEntity]: ...

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
