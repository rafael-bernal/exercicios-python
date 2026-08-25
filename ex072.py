listagem = ('Lápis', 1.75,
            'Borracha', 1.50,
            'Caderno', 12,
            'Tesoura', 3.90,
            'Estojo', 8.90,
            'Caneta', 2,
            'Apontador', 3.50)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end =' ')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-' * 40)