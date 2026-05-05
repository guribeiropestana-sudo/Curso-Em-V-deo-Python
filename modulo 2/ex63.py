x = int(input('Digite quantos termos você quer: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}',end='')
c = 3
while c <= x:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f' -> {t3}', end='')
    c += 1
print(' -> Fim')