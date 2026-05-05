print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
totC = prod1000 =menor =cont =  0
barato = ' '
while True:
    nomep = str(input('Nome do produto: ')).strip()
    precop = float(input('Preço: R$'))
    cont +=1
    totC += precop
    if precop > 1000:
        prod1000 += 1
    if cont == 1:
        menor = precop
        barato = nomep
    else:
        if precop < menor:
            menor = precop
            barato = nomep
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'Total da compra: {totC} reais.')
print(f'Total de produtos que custam mais de 1000 reais: {prod1000}')
print(f'Produto mais barato foi {barato} que custa R${menor}')