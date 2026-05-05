import math
a = float(input('Me de um ângulo qualquer '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O valor do seno é {:.2f}\nO valor do cosseno é {:.2f}\nO valor da tangente é {:.2f}'.format(s,c,t))

