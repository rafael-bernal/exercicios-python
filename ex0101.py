from time import sleep

def maior (* num):
    cont = maior = 0
    print('-'*30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 1, 7, 9, 0)
maior(4, 7)
maior(8, 0)
maior(1, 2)