#IMC - índice de massa corporal
peso = float(input('Qual o seu peso em quilogramas(kg)?  '))
altura = float(input('Qual sua altura em metros(m): '))
imc = peso/(altura*altura)

print(f'O IMC desta pessoa é de {imc:.1f}')

if imc >= 18.5 and imc <= 25:
    print('Peso Ideal')

elif imc >= 25 and imc <= 30:
    print('Sobrepeso')

elif imc >= 40 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')