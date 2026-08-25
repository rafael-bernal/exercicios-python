
num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),)
print(f'Voce digitou {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareçeu na {num.index(3)+1}ªposição')
else:
    print('O valor 3 não foi encontrado')
print('Os valores pares digitados foram', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
