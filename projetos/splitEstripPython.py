import random
print("ROLETA");
entrada = input("Digite suas opçoes separadas por virgulas: ");

#transforma string em lista
lista = entrada.split(",");
#na verdade separa as strings com vírgula

#escolher opçao aleatoria
escolhida = random.choice(lista);

print("A sorteada foi: ", escolhida.strip());
#strip vai apagar os espaços no início e fim
#tipo " texto " = "texto"
