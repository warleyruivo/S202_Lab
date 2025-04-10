from pymongo import MongoClient

class Database:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="transporte"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name):
        return self.db[name]
