from bson import ObjectId
from fastapi import APIRouter
from config.db import collection
from models.items_model import Items
from schemas.itrms_schemas import item_serializer,items_serializer

item_api_router = APIRouter()

@item_api_router.get("/")
async def check():
    return {"status": "OK",'msg':"Router is working"}

# @item_api_router.get("/all")
# async def getAllItems():
#     data= dict(collection.find({}))
#     return {"status":"OK" , "msg":"All items are here", "data":data}
    
@item_api_router.get("/{id}")
async def getParticularItem(id:str):
    data = item_serializer(collection.find_one({"_id":id}))
    if len(data)==0:
        return {"status":"Not Found" , "msg":"No item is there with this id", "data":[]}
    else:
        return {"status":"OK" , "msg":"All items are here", "data":data}
    
# @item_api_router.post("/")
# async def addNewItem(newData : Items ):
#     item =collection.insert_one(dict(newData))
#     x = collection.find_one({"_id":ObjectId(item.inserted_id)})
#     print(x)
#     # data = items_serializer(collection.find_one({"_id":ObjectId(item.inserted_id)}))
#     # if len(data)!=0:
#     #     return {"status":"OK" , "msg":"Item posted successfully", "data":data}
#     # else:
#     #     return {"status":"error", "msg":"Error in posting the data"}
#     return {"status":"OK","data":x}

@item_api_router.delete("/{id}")
async def deleteAnItem(id: str):
    collection.find_one_and_delete({'_id' : ObjectId(id)})
    return {"status":"OK","msg":"Item deleted successfully"}

    

