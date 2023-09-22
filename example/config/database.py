from pymongo import MongoClient

Connection_URL = "mongodb+srv://sitansu:smandal@cluster0.nhfpm6o.mongodb.net/pythonpractice?retryWrites=true&w=majority"

client = MongoClient(Connection_URL)

db = client.todo_app
collection = db['todos']
