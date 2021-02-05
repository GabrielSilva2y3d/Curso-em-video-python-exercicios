# Confederação Nacional de Natação
from datetime import date

ano_nascimento = int(input('Ano de Nascimento: '))
data = date.today()
ano = data.year
atleta_idade = ano - ano_nascimento

print(f'O Atleta tem {atleta_idade} anos.')

if atleta_idade <= 9:
    print('Classificação: MIRIM')

elif atleta_idade > 9 and atleta_idade <= 14:
    print('Classificação: INFANTIL')

elif atleta_idade > 14 and atleta_idade <=  19:
    print('Classificação: JÚNIOR')

elif atleta_idade > 19 and atleta_idade <= 25:
    print('Classificação: SÊNIOR')

else:
    print('Classificação: MASTER')