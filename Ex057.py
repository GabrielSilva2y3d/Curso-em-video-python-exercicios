#Informe o seu sexo
sexo = input('Informe o seu sexo: [M/F]').upper()
while (sexo != 'M') and (sexo != 'F'):
    sexo = input('Dados inválidos. Por favor, informe o seu sexo: ').upper()

print(f'Sexo {sexo} registrado com sucesso!')