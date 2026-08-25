cont = 1
total = 10

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro

while cont <= total:
    print(termo, end=' → ')
    termo += razao
    cont += 1

mais = int(input('\nQuer mostrar mais quantos termos? '))

while mais != 0:
    total += mais

    while cont <= total:
        print(termo, end=' → ')
        termo += razao
        cont += 1

    mais = int(input('\nQuer mostrar mais quantos termos? '))

print('FIM')