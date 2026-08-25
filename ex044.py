num = int(input('Digite um número, e veja sua tabuada: '))
print('Tabuada do Aluno')
print('-'*10)
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))