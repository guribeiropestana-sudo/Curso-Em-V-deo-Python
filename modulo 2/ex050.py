soma = 0
cont = 0
for x in range (1, 7):
    num = int(input('Digite um valor: '))
    if num %2 ==0:
        soma += num
        cont += +1
print(f'Vc informou {cont} números pares e a soma é {soma}')

s = 0
c = 0
for x in range(1,7):
    y = float(input('Escolha um número: '))
    if y%2==0:
        s += y
        c +=+1
print('Total de números: {}\nSoma entre eles: {}'.format(s,c))
