from math import floor
somai = 0
mediai = 0
maiorh = 0
nomeh = ''
mulher20 = 0
for x in range(1,5):
    print('----- {}° PESSOA -----'.format(x))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M] [F]: ')).strip()
    somai += i
    if x == 1 and s in 'Mm':
        maiorh = i
        nomeh = n
    if s in 'Mm' and i > maiorh:
        maiorh = i
        nomeh = n
    if s in 'Ff' and i < 20:
        mulher20 += 1
mediai = somai / 4
print ('A média de idade do grupo: {} anos'.format(floor(mediai)))
print('O nome do homem mais velho é {} ele tem {} anos'.format(nomeh,maiorh))
print('Mulheres com mais de 20 anos: {}'.format(mulher20))