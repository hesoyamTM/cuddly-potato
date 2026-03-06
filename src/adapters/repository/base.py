from abc import ABC, abstractmethod


class ItemRepositoryBase(ABC):
    @abstractmethod
    def create_item(self, item_id: int, q: str):
        pass

    @abstractmethod
    def read_item(self, item_id: int) -> str:
        pass
