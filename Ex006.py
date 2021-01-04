numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
#raizquad = numero ** (1/2)
raizquad = pow(numero, (1/2))
print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raizquad:.1f}')
