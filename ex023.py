from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...') #Faz o computador "pensar"
print('-=-' * 20)
jogador = int(input('Que número eu pensei? ')) #Jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você consegiu me vencer!')
else:
    print('Você perdeu! eu pensei no número {}, e não no {}'.format(computador, jogador))
