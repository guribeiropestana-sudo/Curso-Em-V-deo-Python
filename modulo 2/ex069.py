pes18 = 0
homens = 0
mulh20 = 0
d = ' '
while d not in 'Nn':
    print('-'*20)
    print('Cadastro de pessoa')
    idade = int(input('Digite a sua idade: '))
    if idade > 18:
        pes18 += 1
    sexo = ' '
    while sexo not in 'FfMm':
        sexo =input('Digite seu sexo: [M/F]').strip().upper()[0]
        if sexo in 'Mm':
            homens += 1
        elif idade < 20 and sexo in 'Ff':
            mulh20 += 1
    print('Pessoa cadastrada')
    print('-'*20)
    d = ' '
    if d not in 'Ss':
        while d not in 'Ss':
            d = input('Voce deseja continuar? [S/N]').strip().upper()[0]
            if d in 'Nn':
                break
print('-'*20)
print(f'Pessoas com mais de 18 anos: {pes18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulh20}')