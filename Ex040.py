#Exercicio CLÁSSICO 
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1+nota2)/2

if media >= 7:
    print(f'Sua média foi {media:.1f} APROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media:.1f} RECUPERAÇÃO')
else:
    print(f'Sua média foi {media:.1f} REPROVADO')