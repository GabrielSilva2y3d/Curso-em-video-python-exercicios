#Maior, Menor, Igual

num_1 = int(input('Informe um número: '))#informe o primeiro número
num_2 = int(input('Informe outro número: '))#informe o segundo número

if num_1 > num_2: #Se o primeiro número for maior que o segundo
    print('O primeiro valor é maior.')
elif num_2 > num_1: #Se o segundo número for maior que o primeiro
    print('O segundo valor é maior.')
else: #Se um não é maior ou menor que o outro então são valores iguais.
    print('Ambos os valores são iguais')