# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
for c in range(2, num):
    if num % c != 0:
        print('{} É UM NÚMERO PRIMO!'.format(num))
    else:
        print('{} NÃO É UM NÚMERO PRIMO!'.format(num))
