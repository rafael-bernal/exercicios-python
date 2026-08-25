tentativas = 1
from random import randint
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...') #Faz o computador "pensar"
print('-=-' * 20)
jogador = int(input('Que número eu pensei? ')) #Jogador tenta adivinhar
while jogador != computador:
    tentativas += 1
    jogador = int(input('Tente novamente você errou: '))
print('PARABÉNS, VOCE ACERTOU! e precisou de {} tentativas.'.format(tentativas))