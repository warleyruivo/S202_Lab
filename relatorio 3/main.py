from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex 

# Criar a conexão com o banco de dados
db = Database(database="pokedex", collection="pokemons")

# Instanciar a Pokedex passando o banco de dados
pokedex = Pokedex(db)

# Executar algumas consultas
print("Obtendo todos os Pokémons...")
all_pokemons = pokedex.get_all_pokemons()
print(f"Total de Pokémons encontrados: {len(all_pokemons)}")

print("\nBuscando Pokémon pelo nome (Pikachu)...")
pokemon = pokedex.get_pokemon_by_name("Pikachu")
print(pokemon)

print("\nBuscando Pokémons do tipo 'Fire'...")
fire_pokemons = pokedex.get_pokemon_by_type("Fire")
print(f"Total de Pokémons do tipo 'Fire': {len(fire_pokemons)}")

print("\nBuscando Pokémons com ataque acima de 50...")
strong_pokemons = pokedex.get_pokemon_by_base_stat("Attack", 50)
print(f"Total de Pokémons com ataque >= 50: {len(strong_pokemons)}")

print("\nContando quantidade de Pokémons por tipo...")
pokemon_count = pokedex.count_pokemons_by_type()
print(pokemon_count)