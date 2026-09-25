from random import randint
from operator import itemgetter
from time import sleep

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)
             }

for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

print('<<<RANKING DOS JOGADORES>>>')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking, start=1):
    print(f'{i}º lugar: {v[0]} tirou {v[1]}')