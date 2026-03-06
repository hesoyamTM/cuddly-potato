from src.adapters.repository.base import ItemRepositoryBase


class ItemRepositoryInMemory(ItemRepositoryBase):
    def __init__(self):
        self.items = {}

    def create_item(self, item_id: int, q: str):
        self.items[item_id] = q

    def read_item(self, item_id: int) -> str:
        return self.items[item_id]
