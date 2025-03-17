from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")

class ProductAnalyzer:

    def total_sales_per_day(self):
        """Retorna o total de vendas por dia."""
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        writeAJson(result, "Total de vendas por dia")

    def most_sold_product(self):
        """Retorna o produto mais vendido."""
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido")

    def top_spending_customer(self):
        """Encontra o cliente que mais gastou em uma única compra."""
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Cliente que mais gastou")

    def products_sold_above_one(self):
        """Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidade."""
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_vendido": {"$gt": 1}}},
            {"$sort": {"total_vendido": -1}}
        ])
        writeAJson(result, "Produtos com mais de 1 unidade vendida")
    
    def top_customer_per_day(self):
        """Retorna o cliente que mais comprou em cada dia."""
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ])
        writeAJson(result, "Cliente que mais comprou em cada dia")
