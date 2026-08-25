valores = []

while True:
    num = int(input('Digite um numero: '))

    if num not in valores:
        valores.append(num)
    else:
        print('Este valor ja consta em nosso banco de dados. Tente novamente: ')

    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if escolha in 'N':
        break

print('-' * 15)
print(f'VALORES DIGITADOS: {valores}')
print(f'VALORES EM ORDEM CRESCENTE: {sorted(valores)}')
print('-' * 15)

