n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
x = 0
while x != 5:
    print('=' * 10)
    print((""" OPÇÕES:
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] encerrar programa"""))
    x = int(input('Qual a sua opção? '))

    if x == 1:
        print(f'{n1} + {n2} = {n1+n2}')


    if x == 2:
        print(f'{n1} x {n2} = {n1*n2}')


    if x == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Maior número {maior}')


    if x == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))
print('\033[31mPROGRAMA ENCERRADO!')