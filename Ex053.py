#Palindromo!
frase = input('Digite uma frase: ').upper().strip().replace(" ", "")
reverso = frase[::-1]

print('O inverso de \033[34m{}\033[m é \033[31m{}\033[m'.format(frase, reverso))

if frase == reverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')