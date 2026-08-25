casa = float(input('Qual é o valor da casa?: '))
salário = float(input('Qual é o valor do seu salário?: '))
anos = int(input('Em quantos anos de financiamento?: '))
prestacao = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('Vai lhe custar R${:.2f} mensalmente'.format(prestacao))
if prestacao <= minimo:
    print('EMPRESTIMO CONCEDIDO!')
else:
    print('EMPRESTIMO NEGADO!')