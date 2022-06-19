# Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma.
# Por exemplo, para a sequência: 12 17 4 -6 8 0. a Soma deve ser 35.

def main():
    num = int(input('Digite um numero inteiro: '))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input('Digite mais um numero inteiro: '))
    print('A soma é igual a {}'.format(soma))

main()

#def main():
#    a = 12
#    b = 17
#    c = 4
#    d = -6
#    e = 8
#    f = 0
#    soma = a + b + c + d + e + f
#    print('A soma dos 6 valores é igual a', soma)

#main()

