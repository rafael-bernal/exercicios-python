nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO! Sua média foi {}, foi menor que 5.0'.format(media))
elif media <= 6.9:
    print('RECUPERAÇÃO! Sua média foi de {}, uma boa recuperação!'.format(media))
else:
    print('APROVADO! Meus parabéns, sua média foi de {}, boas férias!'.format(media))