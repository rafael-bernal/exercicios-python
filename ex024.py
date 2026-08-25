v = float(input('Qual a sua velocidade?: '))
if v > 80:
    print('Você foi multado, e sua multa sera de {}'.format((v - 80) * 7))
else:
    print('Você não foi multado, parabéns!')