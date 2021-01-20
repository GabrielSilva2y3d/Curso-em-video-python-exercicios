#Encontre a letra A 
frase = input('Digite uma frase: ').strip().lower()
a = frase.count('a')
primeiroA = frase.find('a')
ultimoA = frase.rfind('a')
print(f'A letra A aparece {a} vezes na frase')
print(f'A primeira letra A aparece na posição {primeiroA+1}')
print(f'A ultima letra A aparece na posição {ultimoA+1}')
