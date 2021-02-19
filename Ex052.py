#Números Primos
num = int(input('Digite um número: '))
cont = 0

for div in range(1,11):
    if num % div == 0:
        print('\033[34m{}\033[m'.format(div), end = "  ")
        cont += 1
    else:
        print('\033[31m{}\033[m'.format(div), end = "  ")
    

print(' ')
if cont <= 2:
    print(f'o numero {num} foi divisível {cont} vezes')
    print(f'{num} É UM NÚMERO PRIMO')
else:
    print(f'o numero {num} foi divisível {cont} vezes')
    print(f'{num} NÃO É UM NÚMERO PRIMO')


