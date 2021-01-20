import time
from random import randint

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
pensando = randint(0,5)
print('-=-'*20)

num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)

if num == pensando:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou. Eu pensei no número {pensando} e não {num}')