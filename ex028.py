s = float(input('Qual é o seu salário? R$'))
if s > 1_250_00:
    print('Você recebeu um aumento de 10%! Seu salário atual é de R${:.2f}'.format(s * 1.10))
else:
    print('Parabéns! Você recebeu um aumento de 15%! Seu salário atual é de R${:.2f}'.format(s * 1.15))