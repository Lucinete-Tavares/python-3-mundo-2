# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

print('\033[93m-=-\033[m' * 10)
print('\033[93m-=- CALCULE SEU EMPRÉSTIMO -=-\033[m')
print('\033[93m-=-\033[m' * 10)

valor = float(input('Digite o valor do imovél: '))
salario = float(input('Quanto você ganha? '))
tempo = int(input('Em quantos anos você irá pagar? '))

tempo = tempo * 12
parcela = valor / tempo

print('\n\033[93mANALIZANDO...\033[m\n')
sleep(3)

if parcela <= salario * 30 / 100:
    print('Emprestimo \033[4;92mAPROVADO!\033[m')
    print('Você pagará \033[93m{}\033[m vezes de \033[91mR$ {:.2f}\033[m!'.format(tempo, parcela))

else:
    print('Empréstimo \033[4;91mREPROVADO!\033[m')
    print('O valor da parecela excedeu 30% da sua renda mensal!')
