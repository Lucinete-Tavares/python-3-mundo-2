# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal, e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# Em 3x ou mais no cartão: 20% de juros

print('=' * 26)
print('-- SISTEMA DE PAGAMENTO --')
print('=' * 26)

preco = float(input('Valor do produto: '))
opcao = int(input('''Opções de pagamento?\n
    >>> 1 Dinheiro
    >>> 2 Debido
    >>> 3 Credito 2X
    >>> 4 Credito 3X ou mais\n'''))

real = preco - (preco * 10 / 100)
debito = preco - (preco * 5 / 100)
credito = preco / 2
credito1 = preco + (preco * 20 / 100)

if opcao == 1:
    print('Valor do produto à vista: R$ {:.2f}'.format(real))

elif opcao == 2:
    print('Valor à vista no cartão: R$ {:.2f}'.format(debito))

elif opcao == 3:
    print('Parecelado em 2X sem juros de: R$ {:.2f}'.format(credito))

elif opcao == 4:
    outro = int(input('Digite o valor das parcelas:\n'))
    print('Parcelado em {}X de: R$ {:.2f}'.format(outro, credito1 / outro))

print('Obrigda e volte sempre!')
