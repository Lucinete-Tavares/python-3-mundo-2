# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.

soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count = count + 1
        soma += c
print('A soma dos {} multiplos de 3 é {}'.format(count, soma))
