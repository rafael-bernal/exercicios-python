dados_escolares = {'Nome': str(input('Nome: ')),
                   'Média': float(input('Sua média: '))}

if dados_escolares['Média'] >= 7:
    dados_escolares['situação'] = 'Aprovado'
else:
    dados_escolares['situação'] = 'Reprovado'

for k, v in dados_escolares.items():
    print(f'{k} é {v}')
