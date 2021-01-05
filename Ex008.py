print('Unidades de Medida')
m = float(input('Digite uma distância em metros: '))
print(f'A distancia de {m}m corresponde a: ')
km = m/1000
hm = m/100
dam = m/10
m = m
dm = m * 10
cm = m * 100
mm = m * 1000

print(f"({km}km - {hm}hm - {dam}dam - {m}m - {dm:.0f}dm - {cm:.0f}cm - {mm:.0f}mm)")

