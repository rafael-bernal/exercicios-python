print('-=-' * 20)
print('Analisador de triãngulos')
print('-=-' * 20)
r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses segmentos PODEM formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES!')
else:
    print('Esses segmentos NÃO PODEM formar um triângulo!')