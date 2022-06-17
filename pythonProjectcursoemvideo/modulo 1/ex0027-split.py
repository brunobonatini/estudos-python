# Faça um programa que leia o nome de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza  primeiro = Ana  ultimo = Souza

nome = input('Digite seu nome: ')
nomedividido = nome.split()
primeiro_nome = nomedividido[0]
ultimo_nome = nomedividido[-1]

print('Seu primeiro nome é',primeiro_nome)
print('Seu último nome é',ultimo_nome)