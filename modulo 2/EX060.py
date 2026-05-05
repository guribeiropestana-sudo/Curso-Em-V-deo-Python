from math import factorial
x = int(input('Digite um valor: '))
c = x
print(f'Fatorial de {x}! ')
while c > 0:
    print(f'{c}',end='')
    print(' x 'if c > 1 else ' = ', end ='')
    c -= 1
print(factorial(x))