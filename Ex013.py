print('Reajuste Salarial')
salario = float(input('Qual o atual salário do funcionario? R$'))
aumento = (salario * 15)/100
reajuste = aumento + salario
print(f'O funcionario recebeu um aumento de 15% e agora seu salario é de R${reajuste:.2f}')
