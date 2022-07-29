# Condições Aninhadas

""" if (condição):
     bloco1
    elif (condição):
     bloco2
    elif (condição):
     bloco3
    else:
     bloco4
"""

nome = str(input('Qual é o seu nome? '))
if nome == 'Bruno':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))