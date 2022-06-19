# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

#numero = int(input('Digite um numero inteiro: '))
#dezena = (numero // 10) % 10

#print('O digito da dezena é: {}'.format(dezena))

numero = input('Digite um numero inteiro: ')

print('O digito da dezena é igual a:',(numero[len(numero)-2]))
