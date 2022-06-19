def main():
    # a_str e b_str guardam string
    a = str(input('Digite o primeiro numero: '))
    b = str(input('Digite o segundo numero: '))

    # a_int e b_int guardam inteiros
    a = int(a) # converteu a string para inteiro
    b = int(b) # converteu b string para inteiro

    # calcule a soma entre valores que são numeros inteiros
    soma = a + b

    # imprima a soma
    print ('A soma de {} + {} é igual a {}'.format(a, b, soma))

main()
