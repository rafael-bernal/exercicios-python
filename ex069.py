times = ('Palmeiras', 'Flamengo', 'Athletico - PR', 'Fluminense', 'Cruzeiro',
         'Bahia', 'Bragantino', 'Athletico - MG', 'Corinthians',
         'Coritiba', 'Botafogo', 'EC Vitória', 'São Paulo', 'Santos',
         'Grêmio', 'Internacional', 'Mirassol', 'Remo', 'Vasco da Gama',
         'Chapecoense')

print('-=-' * 30)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-=-' * 30)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-=-' * 30)
print('Times em ordem alfabética', sorted(times))
print('-=-' * 30)
print(f'A Chapecoense esta na {times.index("Chapecoense") + 1} º posição')