from time import sleep
num = int(input('Digite um número para a criação da tabuada: '))

print('-=-'*5)
for tab in range(1,11,1):
    print(f'{num} x {tab:2} = {tab * num}')
    sleep(0.1)
print('-=-'*5)