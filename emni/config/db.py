from pymongo import MongoClient

MongoURL = "mongodb+srv://sitansu:smandal@cluster0.nhfpm6o.mongodb.net/pythonpractice?retryWrites=true&w=majority"

client = MongoClient(MongoURL)

db = client.emniuser

collection = db["emniuser"]