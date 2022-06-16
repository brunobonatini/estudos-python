idade = int(input('Digite a idade do paciente: '))

if (idade >= 18):
    print('O paciente é maior de idade!')
else:
    print('O paciente é menor de idade.')

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
mediaaluno = (nota1 + nota2) / 2

# verificação
if (mediaaluno >= 7):
    print('A média do aluno é {}. Aprovado!'.format(mediaaluno))
else:
    print('A média do aluno é {}. Reprovado!'.format(mediaaluno))