from fastapi import FastAPI
from pymongo import MongoClient
from pprint import pprint
import urllib.parse

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('root')

app = FastAPI()
client = MongoClient('mongodb', 27017)
# client = MongoClient('mongodb://%s:%s@0.0.0.0:27017' % (username, password))
db = client.hotel
collection = db.booking


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/findall")
async def find_all():
    for each in collection.find():
        pprint(each)


@app.get("/predict{$id}")
async def predict(id):
    print(id)
