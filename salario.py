printf=print;
salario = float(input("Digite o salario: "));
if salario <= 3000:
	printf("Programador Junior");
elif salario > 3000 and salario <= 6000:
	printf("Programador Pleno");
elif salario > 6000 and salario <= 15000:
	printf("Programador Senior");
else:
	printf("Gerente de projetos");