from math import sqrt
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente '))
x = pow(co,2) + pow(ca,2)
print('O comprimento da hipotenusa é {:.1f}'.format(sqrt(x)))
