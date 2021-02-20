#Menu
from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

def menu():
    print('\033[33m   ','=='*5,'★ ','=='*5,'\033[m')
    print('\033[36m    [ 1 ] - SOMAR\n    [ 2 ] - MULTIPLICAR\n    [ 3 ] - MAIOR\n    [ 4 ] - NOVOS NÚMEROS\n    [ 5 ] - SAIR DO PROGRAMA\033[m')
    print('\033[33m   ','=='*5,'★ ','=='*5,'\033[m')

menu()

opcao = int(input('\nEscolha uma opção: '))

while opcao != 5:
    
    if opcao == 1:
        print(f'\nSOMA\n{num1} + {num2} = {num1 + num2}\n')
        menu()
        opcao = int(input('\nEscolha uma opção: '))
    
    if opcao == 2:
        print(f'\nMULTIPLICAR\n{num1} x {num2} = {num1 * num2}\n')
        menu()
        opcao = int(input('\nEscolha uma opção: '))
    
    if opcao == 3:
        print('\nMAIOR NÚMERO')
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}\n')
            menu()
            opcao = int(input('\nEscolha uma opção: '))
        if num1 < num2:
            print(f'Entre {num1} e {num2} o maior valor é {num2}\n')
            menu()
            opcao = int(input('\nEscolha uma opção: '))
    
    if opcao == 4:
            print('\nTROCAR VALORES') 
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            menu()
            opcao = int(input('\nEscolha uma opção: '))
    
    if opcao == 5:
        print('SAINDO DO PROGRAMA . . . ')
        sleep(1.0)
        break

    else:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
        menu()
        opcao = int(input('\nEscolha uma opção: '))

print('PROGRAMA FINALIZADO')