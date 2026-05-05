n = int(input('Digite um valor: '))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[34m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mNúmero: {} é divisível {} vezes'.format(n,tot))
if  tot == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')

n = int (input('Digite um valor: '))
t = 0
for c in range (1, n+1):
    if n % c == 0:
        print('\033[34m',end='')
        t += 1
    else:
        print('\033[31m',end='')
    print(f'{c}',end =' ')
print(f'\n\033[mO número {n} foi divisivel {t} vezes')
if t == 2:
    print('É PRIMO')
else:
    print('Não é primo')



x = int(input('Digite um valor: '))
t = 0
for c in range(1, x+1):
    if x % c:
        print('\033[34m')
        tot += 1
    else:
        print('\033[31m')
print(f'O número {x} foi divisível {tot} vezes')
if tot == 2:
    print('É primo')
else:
    print('Não é primo')