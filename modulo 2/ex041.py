print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO!!!')
idade = int(input('Idade: '))
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade <= 9 or idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade <=14 or idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade <=19 or idade <=25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')