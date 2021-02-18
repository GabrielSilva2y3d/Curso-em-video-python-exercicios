#Soma de números pares
soma = 0
cont = 0
for num in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print(" ")
print(f'Você inseriu {cont} números pares e a soma é igual a {soma}')
    