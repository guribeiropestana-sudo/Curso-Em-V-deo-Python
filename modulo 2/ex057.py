sexo = input('Digite seu sexo: [M/F]').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Digite novamente, dados inválidos: ').strip().upper()[0]
print('Sexo {} adicionado com sucesso!'.format(sexo))

print('Banco do sexo')
sexo = input('Digite seu sexo: [M/F]').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Digite novamente seu sexo').strip().upper()[0]
print('Sexo cadastrado com sucesso')