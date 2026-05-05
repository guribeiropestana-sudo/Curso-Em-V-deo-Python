#lista = []
#for x in range(0,5):
#   x = int(input('Digite um valor '))
#    lista.append(x)
#for i in range(0,len(lista)):
#    md = i
#    for j in range(i+1, len(lista)):
#       if lista[md] > lista [j]:
#            md = j
#    lista[i], lista[md] = lista[md], lista[i]
#print(lista)

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição: {pos}...')
                break
            pos += 1
print(f'Os valores foram: {lista}')