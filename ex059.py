soma = cont = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('Números digitados: {} números'.format(cont))
print('Soma total: {}'.format(soma))