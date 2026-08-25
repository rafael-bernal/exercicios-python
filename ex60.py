soma = 0
cont = 0
resposta = 'S'

while resposta == 'S':
    num = int(input('Digite um valor inteiro: '))

    soma += num
    cont += 1

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

    resposta = input('Quer continuar? [S/N] ').upper()

media = soma / cont

print('A média dos valores digitados foi {:.2f}'.format(media))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
print('Foram digitados {} números'.format(cont))