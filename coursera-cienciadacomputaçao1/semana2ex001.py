#Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado,
# calcule e imprima (saída de dados) seu perímetro e sua área.
#Observação: a saída deve estar no formato: "perímetro: x - área: y"
def main():
    quadrado = int(input('Digite o valor correspondente ao lado de um quadrado '))
    x = quadrado * 4
    y = quadrado ** 2
    print('perímetro:',x, '-', 'área:',y)


main()