# Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

m1 = float(input('Primeiro parâmetro: '))
m2 = float(input('Segundo parâmetro: '))
m3 = float(input('Terceiro parâmetro: '))

if (m1 + m2 > m3) and (m1 + m3 > m2) and (m2 + m3 > m1):
    print('O triângulo que existe é um ', end='')
    if m1 == m2 == m3:
        print('triângulo EQUILÁTERO.')
    elif (m1 == m2) or (m1 == m3) or (m2 == m3):
        print('triângulo ISÓSCELES.')
    else:
        print('triângulo ESCALENO.')
else:
    print('O triângulo inexiste.')
