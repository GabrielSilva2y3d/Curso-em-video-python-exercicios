nome = input('Escreva seu nome completo: ').lower().strip()
silva = 'silva' in nome

if (silva == True):
    print('Seu nome tem "silva"')
else:
    print('Seu nome não tem "silva"')