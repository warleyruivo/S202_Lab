class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def getPokemonByName(self, name: str):
        return self.database.collection.find({"name": name})

    def getPokemonsByType(self, types: list):
        return self.database.collection.find({"type": {"$in": types}})

    def getPokemonsWithEvolutionsByType(self, types: list):
        return self.database.collection.find({"type": {"$in": types}, "next_evolution": {"$exists": True}})

    def getPokemonsByWeaknesses(self, weaknesses: list):
        return self.database.collection.find({"weaknesses": {"$all": weaknesses}})

    def getPokemonsWithSpecificWeaknessesCount(self, size: int):
        return self.database.collection.find({"weaknesses": {"$size": size}})


































































































































































