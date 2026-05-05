n = input('Qual é o seu nome?')
x = {'limpa': '\033[m',
     'preto': '\033[31m'}
print('Olá {}{}{}, seja muito bem vindo!'.format(x['preto'],n, x['limpa']))