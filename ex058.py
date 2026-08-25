num= int(input('Quantos termos você quer mostrar?: '))
a = 0
b = 1
cont = 0
while cont < num:
    print(a, end=' → ')
    c = a + b
    a = b
    b = c
    cont += 1