from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.database = database
    
    def get_all_pokemons(self):
        """Consulta todos os pokémons da coleção."""
        pokemons = list(self.database.collection.find())
        writeAJson(pokemons, "all_pokemons")
        return pokemons
    
    def get_pokemon_by_name(self, name: str):
        """Consulta um pokémon pelo nome."""
        pokemon = self.database.collection.find_one({"name": name}) or {}
        writeAJson(pokemon, f"pokemon_{name}")
        return pokemon
    
    def get_pokemon_by_type(self, type_: str):
        """Consulta todos os pokémons de um determinado tipo."""
        pokemons = list(self.database.collection.find({"type": {"$in": [type_]}}))
        writeAJson(pokemons, f"pokemons_type_{type_}")
        return pokemons
    
    def get_pokemon_by_base_stat(self, stat: str, min_value: int):
        """Consulta todos os pokémons que possuem um valor mínimo para um determinado atributo base."""
        query = {f"base.{stat}": {"$gte": min_value}}
        pokemons = list(self.database.collection.find(query))
        writeAJson(pokemons, f"pokemons_{stat}_gte_{min_value}")
        return pokemons
    
    def count_pokemons_by_type(self):
        """Conta a quantidade de pokémons por tipo."""
        pipeline = [
            {"$unwind": "$type"},
            {"$group": {"_id": "$type", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        result = list(self.database.collection.aggregate(pipeline))
        writeAJson(result, "count_pokemons_by_type")
        return result
