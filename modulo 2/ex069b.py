tot18 =totH =  totM = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'Mm':
        totH += 1
    if idade < 20 and sexo == 'Ff':
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Pessoas com mais de 18 anos: {tot18}')
print(f'Homens cadastrados: {totH}')
print(f'Mulheres com menos de 20 anos: {totM}')