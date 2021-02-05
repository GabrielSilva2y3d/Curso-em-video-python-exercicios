#Valor do Pagamento 
print('============ LOJAS TABAJARA ===========')
preco = float(input('Valor das compras: R$'))

print(' ')
print('FORMAS DE PAGAMENTO')
print('[ 1 ] À VISTA DINHEIRO/CHEQUE')
print('[ 2 ] À VISTA CARTÃO')
print('[ 3 ] 2x NO CARTÃO')
print('[ 4 ] 3x ou mais NO CARTÃO')
print(' ')

desconto_10 = preco - ((preco*10)/100)
desconto_5 = preco - ((preco*5)/100)
juros_20 = preco + ((preco*20)/100)

opcao = int(input('Escolha uma opção: '))
print(' ')

if opcao == 1:
    print(f'Sua compra de R${preco} teve um desconto de 10% e agora vai custar R${desconto_10:.2f}')

if opcao == 2:
    print(f'Sua compra de R${preco} teve um desconto de 10% e agora vai custar R${desconto_5:.2f}')

if opcao == 3:
    print(f'Esse formato não tem descontos seu pagamento é de {preco}')
    
if opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(' ')
    print(f'Sua compra será parcelada em {parcelas}x de R${juros_20/parcelas:.2f} com juros')
    print(f'Sua compra de R${preco} teve um juros de 20% e agora vai custar R${juros_20:.2f}')