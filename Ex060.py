#Calculando fatorial
fat = int(input('Digite um número para calcular seu fatorial: '))
result = 1

print(f'Calculando {fat}! = ',end='')

while fat != 0:
    result = fat * result
    print(fat,end=' x ' if fat > 1 else '')
    fat -= 1

print(' =',result)

    