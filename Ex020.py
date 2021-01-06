import random
print('Sorteando a ordem de apresentação')

aluno1 = input('Escreva o nome do primeiro aluno: ')
aluno2 = input('Escreva o nome do segundo aluno: ')
aluno3 = input('Escreva o nome do terceiro aluno: ')
aluno4 = input('Escreva o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
Ordem = sorted(alunos)
print('A ordem de apresentação dos alunos será:')
print(Ordem)