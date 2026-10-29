def aumentar (preco, taxa, format =False):
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)

def diminuir (preco, taxa, format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)

def dobro (preco, format=False):
    res = preco * 2
    return res if format is False else moeda(res)

def metade (preco, format=False):
    res = preco / 2
    return res if format is False else moeda(res)

def moeda (preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=5, taxar=10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: {moeda(preco)}')
    print('-' *30)
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de Aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de Redução: \t{diminuir(preco, taxar, True)}')

