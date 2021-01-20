#Condição de existência de um triângulo
print('-=-'*10)
print('Analisador de Triângulos ')
print('-=-'*10)

#Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

ladoA = float(input('Digite o valor do lado A: '))
ladoB = float(input('Digite o valor do lado B: '))
ladoC = float(input('Digite o valor do lado C: '))

if (ladoB - ladoC < ladoA < ladoB + ladoC) and (ladoA - ladoC < ladoB < ladoA + ladoC) and (ladoA - ladoB < ladoC < ladoA + ladoB):
    print('Com essas medidas um triângulo PODE ser formado.')
else:
    print('Com essas medidas um triângulo NÃO PODE ser formado.')