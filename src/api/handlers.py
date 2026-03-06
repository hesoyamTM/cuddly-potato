from fastapi import FastAPI

from src.adapters.repository.inmemory import ItemRepositoryInMemory
from src.adapters.repository.base import ItemRepositoryBase
from src.usecases.base import ItemServiceBase
from src.usecases.item_service import ItemService

app = FastAPI()

repository: ItemRepositoryBase = ItemRepositoryInMemory()
service: ItemServiceBase = ItemService(repository)


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item_value = service.read_item(item_id)
    item_value1 = service.read_item(item_id)
    item_value2 = service.read_item(item_id)

    return {
        "item_value": item_value,
        "item_value1": item_value1,
        "item_value2": item_value2,
    }


@app.post("/items")
def create_item(item_id: int, q: str):
    return service.create_item(item_id, q)
