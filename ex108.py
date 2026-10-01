def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')



n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

