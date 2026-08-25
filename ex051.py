soma_idade = 0
media = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome

    if sexo == 'F' and idade < 20:
        totmulher20 += 1

media = soma_idade / 4

print('-=' * 20)
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))