print('Calculando Descontos')
preço = float(input('Digite o preço do produto para calcular o desconto de 5%: R$'))
desconto = (preço * 5)/100
preçoPromoção = preço - desconto

print(f'O preço do protudo com um desconto de 5% fica por R${preçoPromoção:.2f} ')