import random
import os

def jogar_adivinhacao():
    os.system('clear')
    print("\nBem-vindo ao jogo de adivinhação")
    escolha1 = int(input("\nModo normal (1) ou definir intervalos (2)? "))
    if escolha1 == 1:
        normal()
    elif escolha1 == 2:
        personalizado()

def normal():
    numero1 = random.randint(1, 10)
    acertou = False
    tentativas = 0
    limites = 5
    print("\ntente acertar o número que estou pensando")
    print("\nÉ um número entre 1 e 10")
    # limites
    while not acertou and tentativas < limites:
        numero2 = int(input("\nDigite seu palpite: "))
        tentativas += 1
        if numero2 == numero1:
            print(f"\nAcertou! O número que eu pensei foi {numero1}")
            print(f"\nSuas tentativas até agora: {tentativas}")
            acertou = True
        else:
            print(f"\nErrou!")
            if numero2 < numero1:
                print(f"\nSeu número {numero2} é menor ao que eu estou pensando!")
            else:
                print(f"\nSeu número {numero2} é maior ao qual estou pensando!")
            # visualizar
            print(f"\nTentativas restantes: {limites - tentativas}")
    # fim
    if not acertou:
        print(f"\nAcabaram suas tentativas! O número era {numero1}")

def personalizado():
    print("Defina o número minimo e maximo")
    minimo = int(input("Digite aqui o numero do minimo: "))
    maximo = int(input("Digite aqui o numero do maximo: "))
    numero1 = random.randint(minimo, maximo)
    acertou = False
    tentativas = 0
    limites = 5
    print(
        f"Tente acertar o numero que estou pensando, é um numero entre {minimo} e {maximo}"
    )
    # mesmo esquema
    while not acertou and tentativas < limites:
        numero2 = int(input("\nDigite seu palpite: "))
        tentativas += 1
        if numero2 == numero1:
            print(f"\nAcertou! O número que eu pensei foi {numero1}")
            print(f"\nSuas tentativas até agora: {tentativas}")
            acertou = True
        else:
            print(f"\nErrou!")
            if numero2 < numero1:
                print(f"\nSeu número {numero2} é menor ao que eu estou pensando!")
            else:
                print(f"\nSeu número {numero2} é maior ao qual estou pensando!")
            print(f"\nTentativas restantes: {limites - tentativas}")

    if not acertou:
        print(f"\nAcabaram suas tentativas! O número era {numero1}")

while True:
    jogar_adivinhacao()
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Obrigado por jogar")
        break
print("\nFim de jogo")
