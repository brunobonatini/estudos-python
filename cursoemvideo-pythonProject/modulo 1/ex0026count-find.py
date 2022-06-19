# Faça um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
print('A letra a aparece',frase.count('a'),'vezes')
print('A letra a aparece pela primeira vez na posição',frase.find('a'))
print('A letra a aparece a última vez na posição',frase.find('a'))
