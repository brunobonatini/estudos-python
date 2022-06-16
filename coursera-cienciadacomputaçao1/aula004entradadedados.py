temperaturaFahrenheit = input('Digite uma temperatura em F: ')
temperaturaCelsius = (float(temperaturaFahrenheit) - 32) * 5 / 9

print('A temperatura em Celsius é {:.2f}'.format(temperaturaCelsius))

segundos = str(input('Digite a quantidade de segundos a serem convertidos: '))
totalsegundos = int(segundos) # convertendo a variavel segundos de str para int
horas = (totalsegundos // 3600)
segundosrestantes = totalsegundos % 3600
minutos = segundosrestantes // 60
segundosrestantesfinal = segundosrestantes % 60

print ('{} horas {} minutos e {} segundos'.format(horas, minutos, segundosrestantesfinal))

