#Primeiro e Ultimo nome
nomeCompleto = input('Digite o seu nome completo: ').strip().title()
nome = nomeCompleto.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')

