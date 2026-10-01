def fatorial(num=1, show=False):
    f = 1

    for c in range(num, 0, -1):
        f *= c

        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c}', end='')

    if show:
        print(f' = {f}')

    return f


n = int(input('Digite um número: '))
show = input('Mostrar o processo? [S/N] ').upper()

if show == 'S':
    fatorial(n, True)
else:
    print(f'O fatorial de {n} é igual a {fatorial(n)}')
