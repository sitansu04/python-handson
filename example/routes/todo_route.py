from fastapi import APIRouter
from config.database import collection
from models.todo_model import Todo
from schemas.todo_schema import todo_serializer, todos_serializer
from bson import ObjectId

todo_api_router = APIRouter()


@todo_api_router.get("/")
async def check():
    return {"message": "Todo Api is working"}


@todo_api_router.get("/all")
async def get_todo():
    todos = todos_serializer(collection.find())
    print(todos)
    return {"status": "ok", "data": todos}


@todo_api_router.get("/{id}")
async def findone(id: str):
    todo = todos_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": todo}


@todo_api_router.post("/add")
async def add_todo(todo: Todo):
    _id = collection.insert_one(dict(todo))
    todo = todos_serializer(collection.find(
        {"_id": ObjectId(_id.inserted_id)}))
    return {"status": "ok", "msg": "Data inserted", "data": todo}


@todo_api_router.put("/update/{id}")
async def update_todo(id: str, todo: Todo):
    collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
    })
    todo = todos_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "OK", "msg": "Item updated", "data": todo}


@todo_api_router.delete("/delete/{id}")
async def delete_todo(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "OK", "msg": "item deleted succesfully", "data": []}
