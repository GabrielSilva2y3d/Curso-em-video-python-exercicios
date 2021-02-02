#conversor de bases numéricas
#Insira um número inteiro qualquer
num = int(input('Digite um número inteiro qualquer: '))

#convertendo o número inteiro para os valores binário, octal e Hexadeciaml.
binario = str(bin(num))
octal = str(oct(num))
hexadecimal = str(hex(num))

#Informando as escolhas
print('-=-'*10)
print('Escolha uma das bases para a conversão: ')
print(' ')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
print('-=-'*10)
#Informe umas das opções disponiveis 
opcao = int(input('Sua opção: '))

#Escolha entre 1: Binário, 2:Octal e 3:Hexadecimal, qualquer valor além dos informados irá retornar um erro. 
if opcao == 1: #Retorna um valor binário tirando os 2 primeiros valores
    print(f'O número {num} convertido para BINÁRIO é igual a {binario[2:]}')
elif opcao == 2:#Retorna um valor octal tirando os 2 primeiros valores
    print(f'O número {num} convertido para OCTAL é igual a {octal[2:]}')
elif opcao == 3:#Retorna um valor hexadecimal tirando os 2 primeiros valores
    print(f'O número {num} convertido para HEXADECIMAL é igual a {hexadecimal[2:]}')
else:#Retorna uma mensagem de erro
    print('ERRO: Esta opção não está disponivel')
