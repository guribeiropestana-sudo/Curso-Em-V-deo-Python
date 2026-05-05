dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
cor = {'limpa':'\033[m',
       'vermelho':'\033[31m',
       'azul':'\033[32m',
       'amarelo':'\033[33m'}
print('Você nasceu no dia {}{}{}, do mês'.format(cor['vermelho'],dia,cor['limpa']), end=' ')
print('{}{}{} no ano {}{}{}'.format(cor['azul'],mes,cor['limpa'],cor['amarelo'],ano,cor['limpa']))