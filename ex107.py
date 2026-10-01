def ficha (nome = '<desconhecido>', gols = 0):
    print('-'*30)
    if nome == '':
        nome = '<desconhecido>'
    if gols == 3:
        print('UAU! VOCÊ MARCOU UM HAT TRCIK!')
    print(f'O jogador {nome} fez {gols} gols')


n = str(input('Nome do Jogador: '))
ng = (input('Número de Gols: '))

if ng =='':
    ng = 0

ng = int(ng)

ficha(n, ng)