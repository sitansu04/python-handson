from fastapi import FastAPI
from routes.items_route import item_api_router

app = FastAPI()



# @app.get("/")
# async def checkMain():
#     return {"status": "OK", "msg": "API is working"}


app.include_router(item_api_router)