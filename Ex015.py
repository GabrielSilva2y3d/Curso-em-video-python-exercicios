print('Aluguel de carros')
#O carro custa R$60 por dia e R$0,15 por Km rodado.
diasAlu = int(input('Por quantos dias o carro foi alugado? '))
kmRod = float(input('Quantos km rodados?  '))
totpagar = (diasAlu * 60) + (kmRod * 0.15)

print(f'O preço total a pagar ficou R${totpagar:.2f}')
