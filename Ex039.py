#Alistamento Militar 
from datetime import date

#Informando o ano de nascimento
ano_nascimento = int(input('Ano de nascimento: '))
#pegando a data atual
data = date.today()
#pegando o ano atual
ano = data.year
#calculando a idade (ano atual - ano de nascimento)
idade = ano - ano_nascimento

if idade < 18: #se você tem menos de 18 anos 
    print(f'Quam nasceu em {ano_nascimento} tem {idade} anos em {ano}')
    #Calculando a quantidade de anos que ainda faltam para o alistamento
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    #Calculando em que ano poderá fazer o alistamento 
    print(f'Seu alistamento será em {ano + (18 - idade)}')

elif idade == 18:#se você tem 18 anos
    print(f'Quam nasceu em {ano_nascimento} tem {idade} anos em {ano}')
    print('Você tem que se alistar imediatamente')
    
else: #se você tem mais de 18 anos
    print(f'Quam nasceu em {ano_nascimento} tem {idade} anos em {ano}')
    #Calculando a quantidade de anos que deveria ter sido feito o alistamento
    print(f'Você ja deveria ter se alistado há {idade - 18} anos.')
    #Calculando em que ano deveria ter sido feito o alistamento
    print(f'Seu alistamento foi em {ano - (idade - 18)}')



