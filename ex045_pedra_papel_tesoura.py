# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

print('''    REGRAS DO JOGO
-=> Papel vence Pedra e perde para Tesoura
-=> Pedra vence Tesoura e perde para Papel
-=> Tesoura vence Papel e perde para Pedra\n''')

jogador = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")

computador = choice(lista)
vencedor = ""
print('''
Jogador: {}
Computador: {}'''.format(jogador, computador))

if (jogador != "pedra" and jogador != str("papel") and jogador != str("tesoura")):
    print("{} não é uma opção válida. Escolha pedra, papel ou tesoura.".format(jogador))
elif jogador == computador:
    print("Empate. Vamos jogar novamente.")

elif jogador == "pedra" and computador == "tesoura":
    print("Pedra vence tesoura. Jogador ganhou.")

elif jogador == "tesoura" and computador == "pedra":
    print("Pedra vence tesoura. Computador ganhou.")

elif jogador == "pedra" and computador == "papel":
    print("Papel vence pedra. Computador ganhou.")

elif jogador == "papel" and computador == "pedra":
    print("Papel vence pedra. Jogador ganhou.")

elif jogador == "tesoura" and computador == "papel":
    print("Papel vence tesoura. Computador ganhou.")

elif jogador == "papel" and computador == "tesoura":
    print("Papel vence tesoura. Jogador ganhou.")
