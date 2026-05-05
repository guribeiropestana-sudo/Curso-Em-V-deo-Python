lista = []
cont = 0 
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    r = str(input('Deseja continuar? [S/N]')).strip()[0]
    if r not in 'SsNn':
        str(input('Opção inválida.\nDeseja continuar? [S/N]')).strip()[0]
    elif r in 'Nn':
        break
    if 5 in lista:
        cinco = True
    else:
        cinco = False
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: {lista}')
print(f'Quantidade de números digitados foram: {cont}')
if cinco:
    print('Há o valor 5 na lista e está na posição:',end=' ')
    for i,v in enumerate(lista):
        if v == 5:
            print(f'{i +1}...')
else:
    print('Não há o valor 5 na lista.')