import pymongo
from fruitfacts import config


client = pymongo.MongoClient(config.MONGO_URL)
db = client[config.MONGO_DB]