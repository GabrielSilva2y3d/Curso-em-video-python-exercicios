#É ou não santo ???
cidade = input('Em que cidade você nasceu? ')
comecaSanto = cidade.split()#Pega a Primeira palavra
nomeCidade = comecaSanto[0].lower().strip()#Deixa a palavra com letras minusculas e tira os espaços
santo = 'santo' in nomeCidade# Verifica se a primeira palavra é santo

if (santo == True):
     print('Sua cidade começa com "Santo"')
else:
    print('Sua cidade não começa com "Santo"')
