# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
nome_dividido = nome.split()
print('Seu nome com letras maiúsculas: ',nome.upper())
print('Seu nome com letras minúsculas: ',nome.lower())

print('Seu primeiro nome possui',len(nome_dividido[0]),'letras.')