p = int(input('Digite um valor: '))
r = int(input('Digite a razão: '))
c = 0
x = 1
total = 10
while x != 0:
    total += x
    while c < total:
        print(f'{p}',end =' -> ' )
        c += 1
        p += r
    x = int(input('Quer mais? [0 para encerrar] '))
print(f'Você utilizou {total-1} termos na PA\nFim')