

numeros = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

while True:

    escolha = int(input('Escolha um número de 0 até 20: '))

    if 0 <= escolha <=20:
        break

    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[escolha]}')



