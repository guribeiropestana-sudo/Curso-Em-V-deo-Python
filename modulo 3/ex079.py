lista = []
while True:
    x = int(input('Digite um valor: '))
    if x not in lista:
        lista.append(x)
    else:
        print('Valor já existente na lista.')
    r = str(input('Deseja continuar? [S/N]')).strip()[0].upper()
    if r in 'Nn':
        break
lista.sort()
print(f'Lista: {lista}')