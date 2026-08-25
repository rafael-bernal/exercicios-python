from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você nasceu em {} e tem {} anos'.format(nasc,idade))
    print('Este é o ano obrigatório para se alistar!')
elif idade < 18:
    print('Você nasceu em {} e tem {} anos'.format(nasc,idade))
    print('Seu alistamento sera no ano de {}, ainda faltam `{} anos'.format(nasc + 18, 18 - idade))
else:
    print('Você nasceu em {} e tem {} anos'.format(nasc,idade))
    print('Seu alistamento foi há {} anos! no ano de {}'.format(idade - 18, nasc + 18))
    print('Você deve se alistar imediatamente!')
