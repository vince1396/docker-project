from fastapi import FastAPI
from pymongo import MongoClient
from pprint import pprint

app = FastAPI()
client = MongoClient('localhost', '27017')
db = client.booking


@app.get("/findall")
async def find_all():
    for each in db.find():
        pprint(each)
