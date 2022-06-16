#Dados números inteiros n e k, com k >= 0,
#Calcular n elevado a k. Por exemplo, dados os números 3 e 4 o seu programa deve escrever o número 81.

def main():
    n = int(input('Digite o valor de n: '))
    k = int(input('Digite o valor de k: '))

    pot = 1
    i = 0
    while i < k:
        pot = pot * n
        i = i + 1

    print('O valor de {} elevado a {} é igual a {}'.format(n, k, pot))


main()