num = int(input('Digite um número inteiro qualquer: '))
print('''ESCOLHA UMA DAS OPÇÕES ABAIXO
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O numero {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O numero {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida!')