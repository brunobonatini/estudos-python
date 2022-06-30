#Faça um programa que calcule as raízes de segundo grau. (fórmula de bascara)
#Se delta for menor que 0, não existe raízes reais.
#Se delta for igual a 0, existe uma raiz real.
#Se delta for maior que 0, existem 2 raízes reais.

import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = b * b - (4 * a * c)

if (delta < 0):
    print('Não existe raízes reais para esta função.')
elif (delta == 0):
    x = -b / (2 * a)
    print('Existe uma raíz real para esta função x no valor de {}'.format(x))
elif (a != 0):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('Para delta maior que 0 temos duas raízes reais para a função.')
    print('x1 = {:.2f}'.format(x1))
    print('x2 = {:.2f}'.format(x2))
else:
    print('Valor de a inválido.')