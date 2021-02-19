#Progressão Aritmética
from time import sleep

###########################################
print('='*28)
print('    10 TERMOS DE UMA PA      ')
print('='*28)
###########################################

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
fim = primeiro_termo + razao*10

for pa in range(primeiro_termo, fim ,razao):
    print(primeiro_termo, end=" ➔  ")
    primeiro_termo = primeiro_termo + razao
    sleep(0.1)
print('FIM!')

