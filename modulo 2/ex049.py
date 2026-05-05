x = float (input('Digite um valor: '))
ta = 0
for ta in range(1,1001):
    r =  ta* x
    print('{} x {} = {}'.format(x,ta,r))

x = int(input('Número: '))
for c in range(1,11):
    p = x*c
    print('{} x {} = {}'.format(x,c,p))