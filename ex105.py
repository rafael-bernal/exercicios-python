from datetime import date

def voto(a):
    ano = date.today().year
    i = ano - a
    if i < 16:
        return i, 'VOTO NEGADO'
    elif i == 16 or i == 17 or i > 70:
        return i, 'VOTO OPCIONAL'
    else:
        return i, 'VOTO OBRIGATORIO'

ano_nasc = int(input('Em que ano você nasceu?: '))

idade, situacao = voto(ano_nasc)

print(f'Com {idade} anos: {situacao}')







