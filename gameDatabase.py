from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, user, password):
        # Conecta ao banco de dados
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Fecha a conexão com o banco
        self.driver.close()

    # --------------------
    # Jogadores
    # --------------------

    def create_player(self, player_id, name):
        # Cria um novo jogador
        with self.driver.session() as session:
            session.run(
                "CREATE (:Player {id: $id, name: $name})",
                id=player_id, name=name
            )

    def update_player(self, player_id, new_name):
        # Atualiza o nome de um jogador
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {id: $id}) SET p.name = $name",
                id=player_id, name=new_name
            )

    def delete_player(self, player_id):
        # Deleta um jogador e remove suas relações
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {id: $id}) DETACH DELETE p",
                id=player_id
            )

    def get_all_players(self):
        # Retorna todos os jogadores
        with self.driver.session() as session:
            result = session.run("MATCH (p:Player) RETURN p.id AS id, p.name AS name")
            return [record.data() for record in result]

    # --------------------
    # Partidas
    # --------------------

    def create_match(self, match_id, player_ids, result_dict):
        """
        Cria uma partida, conecta jogadores e registra resultado.
        player_ids: lista de IDs dos jogadores
        result_dict: dicionário {player_id: pontuação}
        """
        with self.driver.session() as session:
            # Cria a partida
            session.run(
                "CREATE (:Match {id: $id})",
                id=match_id
            )
            # Relaciona jogadores à partida com resultados
            for pid in player_ids:
                session.run(
                    """
                    MATCH (p:Player {id: $pid}), (m:Match {id: $mid})
                    MERGE (p)-[r:PARTICIPATED_IN]->(m)
                    SET r.score = $score
                    """,
                    pid=pid, mid=match_id, score=result_dict.get(pid, 0)
                )

    def get_match(self, match_id):
        # Retorna detalhes da partida e pontuação de cada jogador
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (p:Player)-[r:PARTICIPATED_IN]->(m:Match {id: $id})
                RETURN m.id AS match_id, p.id AS player_id, p.name AS player_name, r.score AS score
                """,
                id=match_id
            )
            return [record.data() for record in result]

    def delete_match(self, match_id):
        # Deleta uma partida
        with self.driver.session() as session:
            session.run(
                "MATCH (m:Match {id: $id}) DETACH DELETE m",
                id=match_id
            )

    def get_player_match_history(self, player_id):
        # Retorna o histórico de partidas de um jogador
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (p:Player {id: $id})-[r:PARTICIPATED_IN]->(m:Match)
                RETURN m.id AS match_id, r.score AS score
                ORDER BY m.id
                """,
                id=player_id
            )
            return [record.data() for record in result]
