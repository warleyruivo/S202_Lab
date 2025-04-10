from motoristas import Passageiro, Corrida, Motorista
from motorista_dao import MotoristaDAO

class MotoristaCLI:
    def __init__(self):
        self.dao = MotoristaDAO()

    def menu(self):
        while True:
            print("\n[1] Criar Motorista")
            print("[2] Ler Motorista")
            print("[3] Atualizar Motorista")
            print("[4] Deletar Motorista")
            print("[0] Sair")
            opcao = input("Escolha: ")

            if opcao == "1":
                self.criar_motorista()
            elif opcao == "2":
                self.ler_motorista()
            elif opcao == "3":
                self.atualizar_motorista()
            elif opcao == "4":
                self.deletar_motorista()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def criar_motorista(self):
        nota_motorista = int(input("Nota do motorista: "))
        corridas = []

        while True:
            print("\n--- Nova Corrida ---")
            nota = int(input("Nota da corrida: "))
            distancia = float(input("Distância: "))
            valor = float(input("Valor: "))
            nome = input("Nome do passageiro: ")
            documento = input("Documento do passageiro: ")

            passageiro = Passageiro(nome, documento)
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)

            mais = input("Adicionar outra corrida? (s/n): ")
            if mais.lower() != "s":
                break

        motorista = Motorista(nota_motorista, corridas)
        id_inserido = self.dao.create(motorista.to_dict())
        print(f"Motorista inserido com ID: {id_inserido}")

    def ler_motorista(self):
        id = input("ID do motorista: ")
        motorista = self.dao.read(id)
        print(motorista)

    def atualizar_motorista(self):
        id = input("ID do motorista a atualizar: ")
        nova_nota = int(input("Nova nota do motorista: "))
        self.dao.update(id, {"nota": nova_nota})
        print("Motorista atualizado.")

    def deletar_motorista(self):
        id = input("ID do motorista a deletar: ")
        self.dao.delete(id)
        print("Motorista deletado.")
