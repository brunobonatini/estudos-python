import math

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
numero4 = float(input('Digite o quarto número: '))

x1 = numero1
y1 = numero2
x2 = numero3
y2 = numero4
distancia = math.sqrt((x1 ** 2 - x2 ** 2) + (y1 ** 2 - y2 ** 2))
print('A distância entre os dois pontos é igual a {:.2}.'.format(distancia))

if  distancia >= 10:
    print('longe')
else:
    print('perto')