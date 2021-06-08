import creds
from datetime import datetime
from pymongo import MongoClient


if __name__ == "__main__":
    cluster = MongoClient(creds.mongoClient)
    db = cluster[creds.clusterName]
    collection = db[creds.collectionName]

    data = collection.find({})
    for a in data:
        print(a)
