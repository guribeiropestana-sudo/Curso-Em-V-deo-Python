lista = []
listaImpar = []
listaPar = []
while True: 
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]')).strip()[0].upper()
    if resp not in 'SN':
        resp = str(input('Opção inválida.\nDeseja continuar? [S/N]')).strip()[0].upper()
    if resp in 'N':
        break

for x in lista:
    if x %2 == 0:
        listaPar.append(x)

    else:
        listaImpar.append(x)

print(f'Essa foi a lista completa: {lista}')

if listaPar == None:
    print('Não foi digitado valores pares na lista.')

else:
    print(f'Essa foi a lista de valores pares: {listaPar}')

if listaImpar == None: 
    print('Não foi digitado nenhum valor impar na lista.')

else:
    print(f'Essa foi a lista de valores impares: {listaImpar}')