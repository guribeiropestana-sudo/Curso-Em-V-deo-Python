lista = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Ditite mais um valor: ')),
         int(input('Digite o último valor: ')))
if 9 in lista:
    print(f'O valor 9 apareceu {lista.count(9)} vezes')
else:
    print('O valor 9 não apareceu nenhuma vez.')
if 3 in lista:
    print(f'O valor 3 apareceu na posição {lista.index(3)+1}')
else:
    print('O valor 3 não apareceu nenhuma vez.')
print('Os valores pares são:',end=' ')
for x in lista:
    if x %2 == 0:
        print(x, end=' ')
