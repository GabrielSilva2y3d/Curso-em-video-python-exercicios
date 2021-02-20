#Tente adivinhar um numero entre 0 e 10
from random import randint

num = randint(0,10)
cont_tentativas = 0

print('Olá, sou seu computador...\nacabei de pensar em número entre 0 e 10.\nSéra que você consegue adivinhar qual foi?')

adivinhar = int(input('\033[mQual o seu palpite? \033[33m'))

while adivinhar != num:
    if adivinhar > num:
        print('\033[31mUm pouco menos...\033[m\n ')
        adivinhar = int(input('\033[mQual o seu palpite? \033[33m'))
        cont_tentativas += 1
    if adivinhar < num:
        print('\033[34mUm pouco mais...\033[m')
        adivinhar = int(input('\033[mQual o seu palpite? \033[33m'))
        cont_tentativas +=1

print(f'\nVocê acertou em {cont_tentativas} tentativas. Parabéns!\033[m')



