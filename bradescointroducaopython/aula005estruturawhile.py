#A estrutura While (enquanto), executa um determinado conjunto de instruções, enquanto a condição verificada no início permanecer verdadeira.
#Diferente da estrutura For (para), não é necessário determinar o número de vezes que a condição será executada.
#No momento em que a condição for falsa, o processamento da rotina é desviado para fora do laço de repetição.
#Caso a condição seja falsa, logo no início do laço de repetição, as instruções contidas nele são ignoradas.

#Agora, você vai criar uma classe e adicionar à ela um código para exibir os números de 1 a 15 na tela, em ordem crescente:

x = 1;
while x<= 15:
    print(x)
    x = x+1

#É importante observar que, diferente da estrutura For, na estrutura While temos de inicializar a variável antes do início do laço (x=1;).
#E, também, realizar o incremento dentro do bloco de repetição (x=x+1;).

#Para melhor compreensão sobre a estrutura de repetição While, vamos criar uma classe chamada MediaValores, na qual o usuário digita vários valores reais positivos.
#Todos estes números devem ser somados e, quando for digitado algum número negativo, o laço de repetição deverá encerrar e, na sequência, exibir a média dos valores digitados.

quantidade = 0
soma = 0
media = 0
valordigitado = float(input('Digite um valor: '))

while (valordigitado > 0.0):
    soma = soma + valordigitado;
    quantidade = quantidade + 1
    #Entrada de valores
    valordigitado = float(input('DIgite um valor: '))

#Caso digite um valor negativo o laço encerra.

media = soma / quantidade
print('\n Total da soma: {}'.format(soma))
print(' Quantidade de valores digitados: {}'.format(quantidade))
print(' Média dos valores: {}'.format(media))




