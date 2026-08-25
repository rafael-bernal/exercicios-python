from random import randint

lista = []
for c in range(1, 6):
    lista.append(randint(1, 10))

nome_da_tupla = tuple(lista)

print(f'Os valores sorteados foram {nome_da_tupla}')
print(f'O menor número digitado foi {min(nome_da_tupla)}')
print(f'O maior número digitado foi {max(nome_da_tupla)}')