# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior; os dois são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O PRIMEIRO número é MAIOR!')

elif num2 > num1:
    print('O SEGUNDO número é MAIOR!')

else:
    print('\033[31mNÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS!\033[m')
