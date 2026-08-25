from math import sqrt, pow, hypot
co= float(input('Qual é o comprimento do cateto oposto? '))
ca= float(input('Qual é o cateto adjacente? '))
hip= hypot(co,ca)
print('Então a hipotenusa e igual a {}'.format(hip))