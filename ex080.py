expressao = input('Digite uma expressão: ')
contador = 0
correto = True

for caractere in expressao:

    if caractere == '(':
        contador += 1

    elif caractere == ')':
        contador -= 1

        if contador < 0:
            correto = False

if correto and contador == 0:
    print('A expressão esta correta!')

else:
    print('A expressão esta incorreta!')