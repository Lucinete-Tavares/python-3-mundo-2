# Crie um programa que leia uma frase qualquer
# E diga se ela é um palíndromo, desconsiderando os espaços

frase = input('Digite uma frase qualquer: ')
if str(frase) == str(frase)[::-1]:
    print('A frase "{}" é um POLÍNDROMO!'.format(frase))
else:
    print('Esta frase não é um POLÍNDROMO!')
