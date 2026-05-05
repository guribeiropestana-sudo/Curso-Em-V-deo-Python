lista = []
maior = menor =  0
for x in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {x}: ')))
    if x == 0:
        maior = menor = lista[x]
    else:
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < menor:
            menor = lista[x]
print(f'Maior valor {maior} e as suas posições:',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end=' ')

print(f'\nMenor valor {menor} e a suas posições:',end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end=' ')