# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: júnior
# Até 20 anos: sênior
# Acima de 20: master

print('\033[4;34m_\033[m' * 26)
print('\033[4;34mCLASSIFICAÇÃO DE ATLETISMO\033[m')
print('\033[4;34m_\033[m' * 26)

idade = int(input('Quantos anos você tem? '))
if idade <= 9:
    print('Você se encaixa na categoria \033[1;96mMIRIM\033[m')
elif idade <= 14:
    print('Você entrará na categoria \033[1;94mINFÂNTIL\033[m')
elif idade <= 19:
    print('Sua categoria é \033[1;93mJUNIOR\033[m')
elif idade == 20:
    print('Com essa idade você entra na categoria \033[1;34mSÊNIOR\033[m')
else:
    print('Com a sua idade você já é categoria \033[1;92mMASTER\033[m')
