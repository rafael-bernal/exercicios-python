num = int(input('Digite um número qualquer: '))
resultado = 1

while num > 1:
    resultado *= num
    num -= 1

print('O fatorial é {}'.format(resultado))