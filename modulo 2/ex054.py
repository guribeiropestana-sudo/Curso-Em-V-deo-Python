maior = 0
menor = 0
for x in range(1, 8):
    y = int(input('Idade: '))
    if y >= 18:

        maior += +1
    elif y < 18:

        menor += +1
print('Quantidades de pessoas maiores de idade: {}\nQuantidades de pessoas menores de idade: {}'.format(maior,menor))