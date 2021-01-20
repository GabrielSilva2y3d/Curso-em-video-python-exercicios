#Ano bissexto
from datetime import date
ano = int(input('Que ano você quer analisar?(Digite "0" para analisar o ano atual: )'))

data_atual = date.today()

if ano == 0:
    ano = data_atual.year
else:
    ano = ano

if (ano % 4 == 0 and ano % 100 != 0):
    print(f'{ano} é um ano Bissexto')
else:
    print(f'{ano} não é um ano Bissexto')


