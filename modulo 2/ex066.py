c = s = n = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    c +=1
print(f'Soma: {s}\nNúmeros usados: {c}')