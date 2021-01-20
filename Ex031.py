#Valor da passagem
viagem = int(input('Qual a distância da sua viagem em Km: '))

if viagem < 200:
    print(f'O valor da passagem vai ser de R${viagem*0.50:.2f}')
else:
    print(f'O valor da passagem vai ser de R${viagem*0.45:.2f}')

