import os
import time
from dataclasses import dataclass

os.system("cls")

lista_aviao = ["aviao1", "aviao2", "aviao3", "aviao4"]
lista_assento = [0, 0, 0, 0]
reservas = []

@dataclass
class Registro:
    numero_aviao: str
    nome_passageiro: str

def registrar_aviao(lista_aviao):
    print("\n===== Registrar o número de cada avião =====")
    for i in range(4):
        numero = input(f"Informe o número do avião {i+1}: ")
        lista_aviao[i] = numero
    print("\nAviões registrados com sucesso!")


def registrar_qunt(lista_assento):
    print("\n===== Registrar Assentos =====")
    for i in range(4):
        try:
            assentos = int(input(f"Informe a quantidade de assentos do avião {i+1}: "))
            lista_assento[i] = assentos
        except:
            print("Valor inválido!")
    print("\nAssentos registrados com sucesso!")


def reserva_aviao(lista_aviao):
    if len(reservas) >= 20:
        print("\nLimite máximo de reservas atingido!")
        return

    print("\n -- Reserva --")
    reversa = input("\nInforme o avião que deseja reservar: ")

    if reversa not in lista_aviao:
        print("Este avião não existe!")
        return
    indice = lista_aviao.index(reversa)
    if lista_assento[indice] <= 0:
        print("Não há assentos disponíveis para este avião!")
        return
    nome = input("Informe seu nome: ")
    lista_assento[indice] -= 1
    reservas.append(Registro(reversa, nome))
    print("\nReserva registrada com sucesso!")

def consulta_aviao(lista_aviao):
    aviao = input("\nInforme o número do avião: ")

    if aviao not in lista_aviao:
        print("\nEste avião não existe!")
        return

    print(f"\nAvião encontrado: {aviao}")
    print("Reservas para este avião:\n")

    achou = False
    for r in reservas:
        if r.numero_aviao == aviao:
            print(f"- {r.nome_passageiro}")
            achou = True

    if not achou:
        print("Não há reservas realizadas para este avião!")


def consulta_passageiro():
    nome = input("\nInforme o nome do passageiro: ")

    achou = False
    for r in reservas:
        if r.nome_passageiro == nome:
            print(f"- Reserva no avião: {r.numero_aviao}")
            achou = True

    if not achou:
        print("Não há reservas realizadas para este passageiro!")


while True:
    print("""
===== MENU =====
1 - Registrar Aviões
2 - Registrar Assentos
3 - Reservar Passagem
4 - Consultar por Avião
5 - Consultar por Passageiro
6 - Sair
""")
    try:
     opcao = int(input("Informe uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Informe um número...")
        os.system("cls")
        continue

    
    match opcao:
     case 1 :
        registrar_aviao(lista_aviao)
     case 2 : 
        registrar_qunt(lista_assento)
     case 3 :
        reserva_aviao(lista_aviao)
     case 4: 
        consulta_aviao(lista_aviao)
     case 5:
        consulta_passageiro()
     case 6: 
        print("Saindo do programa...")
        time.sleep(3)
        break
     case _:
        print("Opçao invalida")
        
    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)

    if opcao != 0:
        os.system("cls")


