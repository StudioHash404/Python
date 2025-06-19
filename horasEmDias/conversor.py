print("Conversor de horas para dias");
print("-----------------------------");
while True:
  horas = input("\nDigite as horas (ex: 120) ou 'sair' para sair: ");
  if horas == 'sair':
    break;
  if horas.isdigit():
    #caso for True faz este codigo abaixo
    horas = int(horas);
    dias = horas / 24;
    print(f"\n{horas} horas = {dias} dias\n");
  else:
    #caso for False faz este codigo abaixo
    print("Erro! Digite apenas numeros inteiros");
