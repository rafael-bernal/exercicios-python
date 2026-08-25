galera = []
dado = []
cadastros = 0

while True:
    dado.append(str(input('Seu Nome: ')))
    dado.append(int(input('Seu Peso: ')))
    cadastros += 1
    galera.append(dado[:])
    dado.clear()
    continuar = input('Quer continuar? [S/N]: ').upper()

    if continuar == 'N':
        break

maior_peso = galera[0][1]

for p in galera:
    if p[1] > maior_peso:
        maior_peso = p[1]

print(f'Foram cadastrados {cadastros} pessoas na lista!')

print(f'O maior peso foi de {maior_peso}kg')

for p in galera:
    if p[1] == maior_peso:
        print(p[0])

menor_peso = galera[0][1]

for p in galera:
    if p[1] < menor_peso:
        menor_peso = p[1]

print(f'O menor peso foi de {menor_peso}kg')

for p in galera:
    if p[1] == menor_peso:
        print(p[0])







