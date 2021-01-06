import math
print('Teorema de Pitágoras')
catetoOposto = float(input('Cateto Oposto: '))
catetoAdjacente = float(input('Cateto Adjacente'))
hipotenusa = math.sqrt((catetoOposto**2) + (catetoAdjacente**2))
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
 
