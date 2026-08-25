from random import randint
from time import sleep
print('\033[32m-=-\033[m' * 10)
print('     \033[1;33mVAMOS JOGAR JOKENPÔ?\033[m')
print('\033[32m-=-\033[m' * 10)
computador = randint(0, 2)
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
jogador = int(input('QUAL É A SUA JOGADA?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
if computador == jogador:
    print('EMPATE!')
elif jogador == 0 and computador == 1:
    print('VOCÊ PERDEU! Papel ganha da Pedra!')
elif jogador == 0 and computador == 2:
    print('VOCÊ ME VENCEU! Pedra ganha de Tesoura!')
elif jogador == 1 and computador == 0:
    print('VOCÊ ME VENCEU! Papel ganha de Pedra!')
elif jogador == 1 and computador == 2:
    print('VOCÊ PERDEU! Tesoura ganha de Papel!')
elif jogador == 2 and computador == 0:
    print('VOCÊ PERDEU! Pedra ganha de Tesoura!')
elif jogador == 2 and computador == 1:
    print('VOCÊ GANHOU! Tesoura ganha de Papel')
else:
    print('Opção Invalida!')

