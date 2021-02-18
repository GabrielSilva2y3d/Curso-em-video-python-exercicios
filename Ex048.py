#soma dos números ímpares e multiplos de 3
cont = 0
cont_multi = 0
multi = 0

while cont <= 499:
    cont = cont + 1 
    if (cont % 3 == 0) and (cont % 2 != 0):
        cont_multi = cont_multi + 1
        multi = multi + cont

print(f'A soma dos {cont_multi} numeros solicitados é igual a {multi}')



    
    



        



