valores = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))

print(f'O menor valor é {min(valores)}, esta na posição {valores.index(min(valores))}')
print(f'O maior valor é {max(valores)}, esta na posição {valores.index(max(valores))}')