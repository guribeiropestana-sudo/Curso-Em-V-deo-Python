media = qnt = maior = menor = soma = 0
r = 'S'
while r in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    qnt += 1
    if qnt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    r = input('Você deseja continuar? [S/N]')
print(f'Maior: {maior} Menor: {menor}\nQuantidade {qnt}\nSoma: {soma}\nMédia: {soma / qnt}')