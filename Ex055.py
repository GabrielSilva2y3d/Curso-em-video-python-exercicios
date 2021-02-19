#Maior e menor peso
maiorp = 0
menorp = 0
for p in range(1,6):
    peso = float(input(f'informe o peso da {p}ª pessoa em kg:  '))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso

print(f'O maior peso lido foi de {maiorp}Kg')
print(f'O menor peso lido foi de {menorp}Kg')
