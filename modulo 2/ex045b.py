from math import floor
somai = 0
mediag = 0
maiorh = 0
nomeh = ''
mulher20 = 0
for x in range(1,5):
    print('------ {}° PESSOA ------'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M] [F]: '))
    somai += idade
    if x == 1 and sexo in 'Mm':
        maiorh = idade
        nomeh = nome
    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        nomeh = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediag = somai / 4
print('Média de idade: {}'.format(floor(mediag)))
print('Homem mais velho: {}\nIdade: {}'.format(nomeh,maiorh))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(mulher20))