segundos = int(input('Digite a quantidade de segundos a serem convertidos: '))
dias = segundos // 86400
segundosrestantesdias = segundos % 86400
horas = segundosrestantesdias // 3600
segundosrestanteshoras = segundos % 3600
minutos = segundosrestanteshoras // 60
segundosrestantes = segundos % 60


print('{} dias, {} horas, {} minutos e {} segundos.'.format(dias, horas, minutos, segundosrestantes))