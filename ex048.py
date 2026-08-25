frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar)-1, -1, -1):
    inverso += juntar[letra]
print(juntar, inverso)
if inverso == juntar:
    print('É um palindromo')
else:
    print('Não é um palindromo')