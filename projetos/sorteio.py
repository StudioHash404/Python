import random
print("Sorteio");
pessoas = input("Digite o nome das pessoas: ").lower()
lista = pessoas.split(",");
escolhido = random.choice(lista);
print("O ganhador ou ganhadora foi: ", escolhido.strip());
