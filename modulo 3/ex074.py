from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10)
               ,randint(1,10),randint(1,10))
print('A lista dos números: ',end=' ')
for n in numeros:
    print(f'{n}', end = ' ')
print(f'\nO maior valor: {max(numeros)}\nO menor valor: {min(numeros)}')