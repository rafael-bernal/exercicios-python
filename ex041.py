from time import sleep
i = input('Iniciar contagem Regressiva?: ').strip().lower()
if i == 'sim':
    for c in range(10, 0, -1):
        print(c)
        sleep(1)
    print('🎆🎆FELIZ ANO NOVOOO!!!🎆🎆')