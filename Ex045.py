#PEDRA PAPEL OU TESOURA
from random import randint
import time
print('-=-'*5)
print('Suas opções')
print('-=-'*5)
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
print('-=-'*5)
print(' ')

jokenpo = {0: 'PEDRA', 1:'PAPEL', 2:'TESOURA'}

jogada_oponente = randint(0,2)
jogada = int(input('Qual sua jogada? '))

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!')
time.sleep(0.5)

if (jogada == 1 and jogada_oponente == 0) or (jogada == 0 and jogada_oponente == 2) or (jogada == 2 and jogada_oponente == 1):
    print('-=-'*5)
    print(f'Computador jogou {jokenpo[jogada_oponente]}')
    print(f'Jogador jogou {jokenpo[jogada]}')
    print('-=-'*5)
    print('JOGADOR VENCE')

elif (jogada == 0 and jogada_oponente == 1) or (jogada == 2 and jogada_oponente == 0) or (jogada == 1 and jogada_oponente == 2):
    print('-=-'*5)
    print(f'Computador jogou {jokenpo[jogada_oponente]}')
    print(f'Jogador jogou {jokenpo[jogada]}')
    print('-=-'*5)
    print('COMPUTADOR VENCE')

else:
    print('ERRO: JOGADA INVÁLIDA')




