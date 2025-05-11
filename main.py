from database import Database
from gameDatabase import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = GameDatabase("bolt://107.23.86.222:7687", "neo4j", "riddles-byte-linens")
#db.drop_all()

# Criação de jogadores
db.create_player("p1", "Alice")
db.create_player("p2", "Bob")

# Criação de uma partida
db.create_match("m1", ["p1", "p2"], {"p1": 10, "p2": 7})

# Obter todos os jogadores
print(db.get_all_players())

# Detalhes da partida
print(db.get_match("m1"))

# Histórico do jogador
print(db.get_player_match_history("p1"))

# Encerrar conexão
db.close()