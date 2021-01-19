#Sistema de numeração decimal
numero = int(input('Escreva um numero de 0 a 9999: '))
#===============================#
# Extrai a unidade
unidade = numero % 10
# Tirando a unidade do numero 
numero = (numero - unidade)/10
#===============================#
# Extrai a dezena
dezena = numero % 10
# Tirando a dezena do numero
numero = (numero - dezena)/10
#===============================#
# Extrai a centena
centena = numero % 10
# Tirando a centena do numero
numero = (numero - centena)/10
#===============================#
#Resto ---
milhar = numero

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena:.0f}')
print(f'Centena: {centena:.0f}')
print(f'Milhar: {milhar:.0f}')
