from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade <= 9:
    print('Voce tem {} anos, logo, você é uma ATLETA MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, logo, você é uma ATLETA INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, logo, você é uma ATLETA JUNIOR'.format(idade))
elif idade <= 20:
    print('Voce tem {} anos, logo, você é uma ATLETA SENIOR'.format(idade))
else:
    print('Você tem {} anos, ja é uma ATLETA MASTER, parabens!'.format(idade))