valores = []
valores_pares = []
valores_impares = []


while True:
    num= int(input('Digite um valor: '))
    valores.append(num)

    continuar= (input('Quer continuar? [S/N] ')).strip().upper()

    if continuar == 'N':
        break

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

print(f'SUA LISTA GERAL CONTÉM {len(valores)} VALORES')
print(f'{valores}')
print(f'LISTA DE NÚMEROS PARES {valores_pares}')
print(f'LISTA VALORES ÍMPARES {valores_impares}')
