a = input('Informe um valor para a variável a: ')
b = input('Informe um valor para variável b: ')

if (a > b):
    aux = a;
    a = b;
    b = aux;
print('O valor da variável a é {}'.format(a))
print('O valor da variável b é {}'.format(b))
