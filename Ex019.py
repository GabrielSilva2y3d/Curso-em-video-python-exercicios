import random
print('Sorteando Alunos')

aluno1 = input('Escreva o nome do primeiro aluno: ')
aluno2 = input('Escreva o nome do segundo aluno: ')
aluno3 = input('Escreva o nome do terceiro aluno: ')
aluno4 = input('Escreva o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(alunos)

print(f'O(A) aluno(a) escolhido(a) foi {sorteado}')


