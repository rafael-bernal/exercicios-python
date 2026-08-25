preco = float(input('Qual é o valor do produto? R$ '))

print('\033[34m{}\033[m'.format('-=' * 20))
print('      \033[33mFORMAS DE PAGAMENTO\033[m')
print('\033[34m{}\033[m'.format('-=' * 20))

print('[1] À vista (dinheiro/cheque) - 10% de desconto')
print('[2] À vista no cartão         - 5% de desconto')
print('[3] Em até 2x no cartão       - preço normal')
print('[4] 3x ou mais no cartão      - 20% de juros')

opcao = int(input('Digite a opção de pagamento: '))

if opcao == 1:
    valor_final = preco - (preco * 0.10)
    print('O valor final é R$ {:.2f}'.format(valor_final))

elif opcao == 2:
    valor_final = preco - (preco * 0.05)
    print('O valor final é R$ {:.2f}'.format(valor_final))

elif opcao == 3:
    parcelas = 2
    valor_parcela = preco / parcelas
    print('Pagamento em {}x de R$ {:.2f} sem juros'.format(parcelas, valor_parcela))
    print('Valor total: R$ {:.2f}'.format(preco))

elif opcao == 4:
    parcelas = int(input('Em quantas parcelas? (mínimo 3): '))

    if parcelas >= 3:
        valor_total = preco + (preco * 0.20)
        valor_parcela = valor_total / parcelas

        print('Pagamento em {}x de R$ {:.2f} com juros'.format(parcelas, valor_parcela))
        print('Valor total com juros: R$ {:.2f}'.format(valor_total))
    else:
        print('Número de parcelas inválido para essa opção!')

else:
    print('Opção inválida!')
