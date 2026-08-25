total = 0
caros = 0
menor_preco = 0
produto_barato = ''
cont = 0

print('==' * 20)
print('----------LOJA_DO_JUAREZ----------')
print('==' * 20)

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço R$'))

    cont += 1
    total += preco

    if cont == 1:
        menor_preco = preco
        produto_barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            produto_barato = produto

    if preco > 1000:
        caros += 1

    resposta = input('Quer continuar? [S/N] ').strip().upper()

    while resposta not in 'SN':
        print('Resposta inválida, tente novamente')
        resposta = input('Quer continuar? [S/N] ').strip().upper()

    if resposta == 'N':
        print('FINALIZANDO COMPRA...')
        break

print(f'Seu gasto total da compra foi de R${total:.2f}')
print(f'{caros} produtos custam mais de R$1000.00')
print(f'O produto mais barato foi: {produto_barato}')