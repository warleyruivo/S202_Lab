class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return f"Passageiro(nome={self.nome}, documento={self.documento})"


class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def __str__(self):
        return (f"Corrida(nota={self.nota}, distancia={self.distancia}, "
                f"valor={self.valor}, passageiro={self.passageiro.nome})")


class Motorista:
    def __init__(self, nota: int):
        self.nota = nota
        self.corridas = []

    def adicionar_corrida(self, corrida: Corrida):
        self.corridas.append(corrida)

    def __str__(self):
        return (f"Motorista(nota={self.nota}, "
                f"corridas={[str(c) for c in self.corridas]})")
