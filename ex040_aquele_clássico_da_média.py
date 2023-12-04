# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: reprovado
# Média entre 5.0 e 6.9: recuperação
# Média 7.0 ou superior: aprovado

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

if (nota1 + nota2) / 2 >= 70:
    print('\033[1;92mPARABÉNS, VOCÊ FOI APROVADO!\033[m')

elif nota1 + nota2 < 50:
    print('Infelizmente você foi \033[1;91mREPROVADO!\033[m')

else:
    print('A sua média foi {} e você ficou em \033[1;93mRECUPERAÇÃO!\033[m'.format((nota1 + nota2) / 2))
