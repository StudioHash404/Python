# ⏰ Conversor de Horas para Dias

Este é um pequeno programa em Python que converte um valor de horas em dias. Ele roda em um loop interativo, permitindo que o usuário insira quantas vezes quiser — ou digite `sair` para encerrar.

## 🧠 Como funciona

1. O programa exibe uma mensagem de boas-vindas.
2. Em um loop contínuo:
   - Solicita ao usuário que insira um número de horas.
   - Se o usuário digitar `sair`, o programa termina.
   - Se o valor inserido for um número inteiro, ele é convertido em dias (`horas ÷ 24`) e exibido.
   - Se o valor não for um número válido, o programa mostra uma mensagem de erro.

## 💻 Exemplo de uso

```bash
Digite as horas (ex: 120) ou 'sair' para sair: 48

48 horas = 2.0 dias
```

## 🧾 Código fonte

```python
print("Conversor de horas para dias")
print("-----------------------------")

while True:
  horas = input("\nDigite as horas (ex: 120) ou 'sair' para sair: ")
  
  if horas == 'sair':
    break

  if horas.isdigit():
    horas = int(horas)
    dias = horas / 24
    print(f"\n{horas} horas = {dias} dias\n")
  else:
    print("Erro! Digite apenas numeros inteiros")
```

## 🚀 Requisitos

- Python 3 instalado no sistema.

## ✅ Como executar

1. Salve o código em um arquivo chamado `conversor.py`.
2. No terminal, execute:

```bash
python conversor.py
```
