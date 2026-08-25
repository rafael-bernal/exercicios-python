maiores18= 0
homens = 0
mulheres20 = 0

while True:
    idade = int(input('Qual a sua idade? '))
    sexo = (input('Qual o seu sexo? [M/F] ')).strip().upper()

    while not sexo in 'MF':
        print('Opção invalida, tente novamente')
        sexo = (input('Qual o seu sexo? [M/F] ')).strip().upper()

    if idade > 18:
        maiores18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    resposta = (input('Deseja continuar? [S/N] ')).strip().upper()

    while not resposta in 'SN':
        print('Resposta invalida, tente novamente')
        resposta = (input('Deseja continuar? [S/N] ')).strip().upper()

    if resposta == 'N':
        print('ENCERRANDO...')
        break

print(f'A) Existem {maiores18} maiores de 18 anos')
print(f'B) Existem {homens} homens cadastrados')
print(f'C) Existem {mulheres20} mulheres com menos de 20 anos')