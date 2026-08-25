from random import randint

vitorias = 0

print('==' * 18)
print('----- VAMOS JOGAR PAR OU ÍMPAR -----')
print('==' * 18)

while True:
    valor = int(input('Digite um valor: '))
    jogador = input('Você quer [P/I]? ').strip().upper()

    while jogador not in ('P', 'I'):
        print('Opção inválida!')
        jogador = input('Você quer [P/I]? ').strip().upper()

    computador = randint(0, 10)
    soma = valor + computador

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print('-' * 35)
    print(f'Você jogou {valor} e o computador jogou {computador}.')
    print(f'Total de {soma} DEU {resultado}.')
    print('-' * 35)

    if (resultado == 'PAR' and jogador == 'P') or (resultado == 'ÍMPAR' and jogador == 'I'):
        vitorias += 1
        print('VOCÊ GANHOU! Vamos tentar novamente...')
    else:
        print('GAME OVER! VOCÊ PERDEU!')
        break

print(f'Você venceu {vitorias} vezes consecutivas.')