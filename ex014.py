from math import radians, sin, cos, tan, floor, ceil
num= float(input('>>>Digite o valor de um angulo: '))
sina= sin(radians(num))
cosang= cos(radians(num))
tanang= tan(radians(num))
print('O valor de seno é {:.2f}, o de cosseno é {:.2f}, e o da tangente é {:.2f}'.format(sina, cosang,tanang))
