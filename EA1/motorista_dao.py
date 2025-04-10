from bson import ObjectId
from database import Database

class MotoristaDAO:
    def __init__(self):
        self.db = Database()
        self.collection = self.db.get_collection("motoristas")

    def create(self, motorista: dict):
        return self.collection.insert_one(motorista).inserted_id

    def read(self, motorista_id: str):
        return self.collection.find_one({"_id": ObjectId(motorista_id)})

    def update(self, motorista_id: str, novos_dados: dict):
        return self.collection.update_one(
            {"_id": ObjectId(motorista_id)},
            {"$set": novos_dados}
        )

    def delete(self, motorista_id: str):
        return self.collection.delete_one({"_id": ObjectId(motorista_id)})
