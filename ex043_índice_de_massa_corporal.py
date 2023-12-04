# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, e acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# Acima de 40: obesidade mórbida

print('>>>>>>>>>>>>  CALCULADORA DE IMC <<<<<<<<<<<<')
print('=' * 45)
print('''      IMC            CLASSIFICAÇÃO     (GRAU)\033[m
MENOR QUE 18,5	        \033[95mMAGREZA\033[m	          0
ENTRE 18,5 E 24,9	    \033[92mNORMAL\033[m	          0
ENTRE 30,0 E 39,9	    \033[93mOBESIDADE\033[m	      II
MAIOR QUE 40,0	        \033[91mOBESIDADE GRAVE\033[m	  III''')
print('=' * 45)

altura = float(input('\n\033[34mAltura (ex.: 1,70)?\033[m '))
peso = float(input('\033[34mPeso (ex.: 69,2)?\033[m '))

imc = peso / altura ** 2

if imc < 18.5:
    print('\nVocê pesa {}kg, seu IMC é {:.2f} e você esta \033[91mABAIXO\033[m do peso!'.format(peso, imc))
elif imc >= 18.5 and imc <= 24.9:
    print('\nVocê pesa {}kg, seu IMC é {:.2f} e você esta \033[94mNORMAL'.format(peso, imc))
elif imc >= 30 and imc <= 39.9:
    print('\nVocê pesa {}kg, seu é {:.2f} você esta \033[95mOBESO\033[m'.format(peso, imc))
else:
    print('\nVocê esta pesando {}kg, o seu imc é {:.2f} e você Possue \033[91mOBESIDADE MÓRBIDA\033[m,'
          'Procure um especialista!'. format(peso, imc))
