galera = []
dado = []
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Digite um Nome: ')))
    dado.append(int(input('Digite sua Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 19:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade, e {totmen} menores de idade')