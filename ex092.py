from datetime import date

dados = {'Nome': str(input('Nome: ')),
         'Ano_nasc': int(input('Ano de Nascimento: ')),
         'CTPS': int(input('Carteira de Trabalho: ')),
         }
idade = date.today().year - dados['Ano_nasc']

dados['idade'] = idade

if dados['CTPS'] != 0:
    dados['Ano_de_contrat'] = int(input('Ano de contratação: '))
    dados['Salário'] = str(input('Salário: R$'))
    idade_aposentadoria = (dados['Ano_de_contrat'] + 35) - dados['Ano_nasc']
    dados['idade_aposentadoria'] = idade_aposentadoria

print('-=-' * 20)

print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
