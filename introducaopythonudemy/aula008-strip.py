a = 'Bruno'
b = 'Leticia'

concatenar = a + ' ' + b + '\n' # \n é uma queba de linha
print(concatenar.strip())

minha_string = 'O rato roeu a roupa do rei de Roma'
minha_lista = minha_string.split('r') # separa a string por espaço removendo a letra r
print(minha_lista)

busca = minha_string.find('rei')
print(busca) # mostra o indice em que a palavra rei se encontra na string = 23
print(minha_string[busca:]) # mostra a string na posição de busca em diante = rei de Roma

minha_string = minha_string.replace('o rei','a rainha')
print(minha_string)