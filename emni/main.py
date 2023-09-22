from config.db import collection
from fastapi import FastAPI
from bson import json_util
from models.emnimodel import Emni
from bson import ObjectId
from flask import Flask, jsonify
import json

app = FastAPI()


@app.get("/")
def getAll():
    data_cursor = collection.find({})
    data_list = [document for document in data_cursor]
    print(data_list)
    return {"status": "OK", "data": json.loads(json_util.dumps(data_list))}, 200


@app.post("/")
def addData(newData: Emni):
    new_data_dict = newData.model_dump()
    result = collection.insert_one(new_data_dict)
    new_data_dict["_id"] = str(ObjectId(result.inserted_id))
    new_key = "_id"
    new_value = new_data_dict["_id"]
    new_dict = {new_key: new_value, **new_data_dict}

    response_data = {"status": "OK", "msg": "Data inserted", "data": new_dict}
    response_code = 201

    response = jsonify(response_data)
    response.status_code = response_code

    return response



@app.delete("/{id}")
def deleteData(id: str):
    x = collection.find_one_and_delete({"_id": id})
    print(x)
    return {"status": "OK"}, 200
