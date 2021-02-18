#Contagem regressiva
import time
def pausa():  
    time.sleep(0.5)

contador = 10

while contador >= 0:
    pausa()
    print(contador)
    contador = contador - 1

print('Fim da Contagem')

    