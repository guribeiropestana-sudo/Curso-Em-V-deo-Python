cont = x = soma = 0
while x != 999:
    soma += x
    cont += 1
    x = int(input('digite um valor: [999 para parar]'))
print(f'Números digitados: {cont-1}\nA soma: {soma}\nFim.')