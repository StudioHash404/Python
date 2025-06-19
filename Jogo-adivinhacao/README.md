# 🎮 Jogo de Adivinhação (Python)

Este é um projeto simples de **jogo de adivinhação** em Python, onde o jogador precisa descobrir o número que o computador está pensando.

---

## 📌 Funcionalidades

- ✅ Dois modos de jogo:
  - **Modo Normal** → número entre 1 e 10
  - **Modo Personalizado** → o jogador escolhe o intervalo
- ✅ Máximo de 5 tentativas por partida
- ✅ Mensagens que indicam se o palpite foi maior ou menor
- ✅ Sistema de repetição automática: pergunta se o jogador quer jogar novamente
- ✅ Limpeza de tela automática com `os.system('clear')` (Linux/macOS)

---

## 🧠 Como funciona o código

O código está organizado em funções:

### 🔹 `jogar_adivinhacao()`
Função principal. Exibe o menu e chama o modo de jogo escolhido pelo usuário.

### 🔹 `normal()`
Gera um número aleatório entre 1 e 10. O jogador tenta adivinhar esse número em até 5 tentativas.

### 🔹 `personalizado()`
Permite que o jogador defina um intervalo mínimo e máximo. O número sorteado estará dentro desse intervalo.

### 🔁 Loop principal
Depois que o jogador joga, ele é perguntado se deseja tentar novamente. Se digitar "s", o jogo recomeça. Se digitar "n", o programa encerra com uma mensagem de agradecimento.

---

## 🖥️ Como rodar o jogo

1. Instale o Python (versão 3.6 ou superior).
2. Clone este repositório:
   ```bash
   git clone https://github.com/StudioHash404/C.git
   ```
3. Acesse a pasta e execute o arquivo:
   ```bash
   cd C
   python nome_do_arquivo.py
   ```

---

## ✅ Exemplo de uso

```text
Bem-vindo ao jogo de adivinhação
Modo normal (1) ou definir intervalos (2)? 1

tente acertar o número que estou pensando
É um número entre 1 e 10

Digite seu palpite: 5
Errou!
Seu número 5 é menor ao que eu estou pensando!
Tentativas restantes: 4
...
```

---

## 🧑‍💻 Autor

Desenvolvido por [StudioHash404](https://github.com/StudioHash404)
