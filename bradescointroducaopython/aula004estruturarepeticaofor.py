# Criando uma classe e adicionando um código que percorre e exibe os numeros de 0 até 9 na ordem crescente.

for n in range(10):
    print(n)

#No exemplo que acabamos de ver, a variável n é inicialmente ajustada para 0 (inicialização com valor padrão).
#Uma vez que n é menor do que 10 (condição), o comando print é executado.
#Essa condição é adicionada com o comando range.
#A variável n é incrementada em 1 (incremento padrão) e é testado se o valor de n ainda é menor do que 10.
#O processo se repete até que o valor de n fique maior ou igual a 10.
#Neste instante, o laço termina e o programa segue a execução das instruções do bloco de repetição.

#Por padrão, o valor inicial do laço de repetição é 0.
#Podemos alterar esse valor no comando range. EX: iniciando em 5 e terminando em 15.

for n in range(5, 16):
    print(n)

#Também é possível utilizar o decremento no contador, dentro do comando range. Tornando a ordem decrescente.

for n in range(10, 0, -1):
    print(n)

