import math
print('Seno, Cosseno e Tangente')
angulo = int(input('Digite um ângulo: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'O Seno do ângulo de {angulo}° vale {seno:.2f}')
print(f'O Cosseno do ângulo de {angulo}° vale {cosseno:.2f}')
print(f'A tangente do ângulo de {angulo}° vale {tangente:.2f}')
