idade = int(input('Digite a idade do paciente: '))

if (idade >= 18):
    print('Paciente maior de idade.')
elif (idade >= 14):
    print('Paciente juvenil.')
else:
    print('Paciente menor de idade.')