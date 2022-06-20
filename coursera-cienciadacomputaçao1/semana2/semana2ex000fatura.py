nomecliente = input('Digite o nome do cliente: ')
diavencimento = input('Digite o dia de vencimento da fatura: ')
mesvencimento = input('Digite o mês de vencimento da fatura: ')
valorfatura = input('Digite o valor da fatura: ')

print('Olá, {}'.format(nomecliente))
print('A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.'.format(diavencimento, mesvencimento,valorfatura))