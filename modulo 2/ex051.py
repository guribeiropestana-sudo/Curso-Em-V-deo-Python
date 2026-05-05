p= int(input('1° Termo: '))
r = int(input('Razão: '))
d = p+(10-1)*r
for x in range (p,d+r,r):
    print(x ,  end=' -> ')
print('Acabou')

