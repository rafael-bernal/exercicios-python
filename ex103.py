def contador (i,f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

help(contador)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1= somar(10, 20, 30)
r2 = somar(3, 4)
r3= somar(9, 2)
r4= somar(3)

print(f'Meus cálculos de soma deram, {r1}, {r2}, {r3}, {r4}')
