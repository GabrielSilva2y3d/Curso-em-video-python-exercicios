#Analisador Completo
media_idade = 0
maior_idade = 0
maior_idade_nome = str('nome')
cont_M_menos_20 = 0

for i in range(1,5):
    print(f'\033[m---- {i}ª PESSOA ----')
    nome = input('\033[mNome: \033[34m',)

    try:
        idade = int(input('\033[mIdade: \033[34m'))
        media_idade = media_idade + idade 
    except ValueError:
        print('\033[31mVocê so pode colocar sua idade em números neste campo\033[m')
        break

    sexo = input('\033[mSexo [M/F]: \033[34m').upper()
    if (sexo != 'M') and (sexo != 'F'):
        print('\033[31mVocê só pode colocar "M" ou "F" nesse campo.\033[m')
        break
    
    if (sexo == 'M') and (maior_idade < idade):
        maior_idade = idade
        maior_idade_nome = nome
    
    if (sexo == 'F') and (idade < 20):
        cont_M_menos_20 += 1

    print('\033[m---'*6)

print('A média de idade do grupo é de {} anos.'.format(media_idade/4))
print('O homem mas velho do grupo tem {} anos e se chama {}.'.format(maior_idade, maior_idade_nome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont_M_menos_20))