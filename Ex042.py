#EQUILÁTERO, ISÓSELES, ESCALENO 
print('-=-'*10)
print('Analisador de Triângulos ')
print('-=-'*10)

ladoA = float(input('Digite o valor do lado A: '))
ladoB = float(input('Digite o valor do lado B: '))
ladoC = float(input('Digite o valor do lado C: '))

if (ladoB - ladoC < ladoA < ladoB + ladoC) and (ladoA - ladoC < ladoB < ladoA + ladoC) and (ladoA - ladoB < ladoC < ladoA + ladoB):
    print('Com essas medidas um triângulo PODE ser formado.')
else:
    print('Com essas medidas um triângulo NÃO PODE ser formado.')

if ladoA == ladoB == ladoC:
    print('Isso é um triângulo EQUILÁTERO')

elif (ladoA == ladoB and ladoA != ladoC) or (ladoA == ladoC and ladoA != ladoB) or (ladoB == ladoC and ladoB != ladoA):
    print('Isso é um triângulo ISÓSELES')

else:
    print('Isso é um triângulo ESCALENO')