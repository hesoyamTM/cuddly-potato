from src.usecases.base import ItemServiceBase
from src.adapters.repository.base import ItemRepositoryBase


class ItemService(ItemServiceBase):
    def __init__(self, repository: ItemRepositoryBase):
        self.repository = repository

    def create_item(self, item_id: int, q: str):
        self.repository.create_item(item_id, q)
        pass

    def read_item(self, item_id: int) -> str:
        q = self.repository.read_item(item_id)
        return q
