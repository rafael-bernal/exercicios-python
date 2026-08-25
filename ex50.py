maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('-=' * 20)
print('O maior peso foi {:.1f} kg'.format(maior))
print('O menor peso foi {:.1f} kg'.format(menor))