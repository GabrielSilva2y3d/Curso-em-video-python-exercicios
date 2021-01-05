print('Pintando a parede')
largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura * altura
litrotinta = area/2
print(f'Sua parede tem uma área de {area:.2f}m²')
print(f'É preciso {litrotinta:.2f}l de tinta para pinta-la.')

