#Maior e Menor
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))

#Maior numero usando if
maior = num1
if (maior < num2):
    maior = num2

if (maior < num3):
    maior = num3

print(f'O maior valor digitado foi {maior}')

#Menor numero usando if
menor = num1
if (menor > num2):
    menor = num2
    
if (menor > num3):
    menor = num3

print(f'O menor valor digitado foi {menor}')