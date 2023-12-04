# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('\033[93mCONVERSOR DE BASES NUMÉRICAS\033[m')
print('\033[93;43m \033[m' * 28)

num = int(input('\nDigite um número qualquer: '))
base = int(input('''Escolha uma das opções abaixo:\n
   \033[93m>>>\033[m 1 para Binário
   \033[93m>>>\033[m 2 para Octal
   \033[93m>>>\033[m 3 para Hexadecimal\n'''))

if base == 1:
    print('\033[4;93mCONVERSÃO BINÁRIA\033[m')
    print('O número {} convertido é igual a \033[34m{}\033[m'.format(num, bin(num)[2:]))

elif base == 2:
    print('\033[4;93mCONVERSÃO OCTAL\033[m')
    print('O número {} convertido é igual a \033[34m{}\033[m'.format(num, oct(num)[2:]))

elif base == 3:
    print('\033[4;93mCONVERSÃO HEXADECIMAL\033[m')
    print('O número {} convertido é igual {}'.format(num, hex(num)[2:]))

else:
    print('\033[1;91mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
