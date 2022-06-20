# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

#numero = int(input('Digite um numero inteiro: '))
#dezena = (numero // 10) % 10

#print('O digito da dezena é: {}'.format(dezena))

numero = int(input('Digite um número inteiro: '))
dezena = (numero // 10) % 10

if (numero > 0):
    print('O dígito das dezenas é {}.'.format(dezena))
else:
    (print('O dígito das dezenas é 0.'))
