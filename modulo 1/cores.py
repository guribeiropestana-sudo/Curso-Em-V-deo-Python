n = input('Qual o seu nome?')
cor = {'limpa':'\033[m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo':'\033[33m',
       'azul':'\033[34m',
       'magenta':'\033[35m',
       'ciano':'\033[36m',
       'cinza':'\033[37m',
       'pretoebranco':'\033[7;30m'}
print('Prazer em te conhecer, {}{}{}'.format(cor['vermelho'],n,cor['limpa']))
print('Eu te amo {}{}{}\nEu te amo {}{}{}'.format(cor['verde'],n,cor['limpa'],cor['amarelo'],n,cor['limpa']))
print('Eu te amo {}{}{}\nEu te amo {}{}{}'.format(cor['azul'],n,cor['limpa'],cor['magenta'],n,cor['limpa']))
print('Eu te amo {}{}{}\nEu te amo {}{}{}'.format(cor['ciano'],n,cor['limpa'],cor['cinza'],n,cor['limpa']))
print('Eu te amo {}{}{}'.format(cor['pretoebranco'],n,cor['limpa']))