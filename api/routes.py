from fastapi import FastAPI
from pymongo import MongoClient
from pprint import pprint

app = FastAPI()
client = MongoClient('db', 27017)
db = client.hotel
collection = db.booking


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/findall")
async def find_all():
    for each in collection.find():
        pprint(each)
