from src.adapters.repository.base import ItemRepositoryBase


class ItemRepositoryPostgres(ItemRepositoryBase):
    def create_item(self, item_id: int, q: str):
        print("Postgres")
        pass

    def read_item(self, item_id: int) -> str:
        print("Postgres")
        return "item"
