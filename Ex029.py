#Velocimetro 
vel = int(input('Velocidade do seu carro em km/h: '))
multa = (vel - 80)*7
if vel < 80:
    print('Esta dentro do limite de velocidade, Tenha um bom dia.')
else:
    print('Você excedeu o limete de velocidade permitido!(80km/h)')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')