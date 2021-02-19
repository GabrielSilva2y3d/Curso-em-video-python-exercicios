#Grupo de Maioridade
import datetime
ano = datetime.date.today().year
maior = 0 
menor = 0

for i in range (1,8):
    ano_nasimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if (ano - ano_nasimento) >= 18:
        maior += 1
    else:
        menor += 1

print(f'\nAo todo tivemos {maior} pessoas maior de idade e\n{menor} pessoas  menor idade')
