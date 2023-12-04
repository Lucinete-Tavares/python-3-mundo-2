# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('TABUADA DE: '))
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(num, c, num * c))
