cont = 1
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
while cont <= 10:
    print(termo, end=' → ')
    termo += razao
    cont += 1
print('FIM')