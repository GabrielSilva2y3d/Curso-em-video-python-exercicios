#emprestimo 
#Insira o valor da casa em reais:
valor_Casa = float(input('Qual o valor da casa? R$'))
#Insira o valor do seu salário em reais:
salario = float(input('Quanto é o seu salário? R$'))
#Informe em quantos anos o emprestimo sera dividido 
anos_pagamento = int(input('Quantos anos de finaciamento? '))
#Valor da prestação mensal. (Passando de anos para meses)
prestação_mensal = valor_Casa/ (anos_pagamento * 12)
#separando 30% do salário 
salario_30 = (salario * 30)/100

#Se a prestação mensal do salario for MENOR ou IGUAL a 30% do salário o emprestimo pode ser concedido, caso contrario não. 
if prestação_mensal <= salario_30:
    print(f'A prestação mensal será de R${prestação_mensal:.2f}')
    print(f'CONDIÇÕES ATENDIDAS: empréstimo pode ser concedido.')
else:
    print(f'A prestação mensal será de R${prestação_mensal:.2f}')
    print(f'CONDIÇÕES NÃO ATENDIDAS: empréstimo não pode ser concedido.')