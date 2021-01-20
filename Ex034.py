#Aumento de salario
salario = float(input('Digite o salario para receber o aumento: R$'))
aumento10 = (salario*10)/100
aumento15 = (salario*15)/100

if (salario > 1250):
    print(f'O salario de R${salario:.2f} ganhou um aumento de 10% e agora é R${salario+aumento10:.2f} ')
else:
    print(f'O salario de R${salario:.2f} ganhou um aumento de 15% e agora é R${salario+aumento15:.2f}')