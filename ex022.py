#manipulando strings

nome = input('Escreva o seu nome completo: ')
print(f'Seu nome completo maiuscolo é {nome.upper()}')
print(f'Seu nome completo minusculo é {nome.lower()}')
print(f'Seu nome tem {len(nome)} letras')

pnome = nome.split()
print(f'Seu primeiro nome é {pnome[0]} que tem {len(pnome[0])} letras')

