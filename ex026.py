d = float(input('Qual é a distância da viagem: '))
if d <= 200:
    print('Você percoreu {}km, e por cada km é cobrado R$0.50, então sua viagem, custou R${}'.format(d, d*0.5))
else:
    print('Sua viagem foi mais longa que 200km, então é cobrado R$0.45 por km, logo sua viagem custou R${}'.format(d*0.45))