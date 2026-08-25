peso= float(input('Informe o seu peso (kg): '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é {:.1f}' .format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Parabens voce esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Voce está em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE')
else:
    print('Voce esta em OBESIDADE MÓRBIDA!')