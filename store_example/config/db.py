from pymongo import MongoClient

Mongo_URL = "mongodb+srv://sitansu:smandal@cluster0.nhfpm6o.mongodb.net/pythonpractice?retryWrites=true&w=majority"

client = MongoClient(Mongo_URL)

db = client.items

collection = db["items"]
