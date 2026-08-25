valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)

    continuar = input('Quer continuar? [S/N] ').upper()

    if continuar == 'N':
        break

if 5 in valores:
    print('O valor 5 apareceu na lista. E esta nas posições')

    for pos, valor in enumerate(valores):
        if valor == 5:
            print(pos)
else:
    print('O número 5 não foi encontrado na lista')

print(f'Você digitou {len(valores)} NÚMEROS!')
print('ORDEM DECRESCENTE')
valores.sort(reverse=True)
print(f'{valores}')
