n = int(input('Me dê um número '))
cor = {'limpa':'\033[m',
       'azul':'\033[34m'}
print('O seu dobro é {}{}{}'.format(cor['azul'],(n*2),cor['limpa']),end=' ')
print('\nO seu tripli é {}{}{}\nA sua raiz quadrada é {}{:.1f}{}'.format(cor['azul'],(n*3),cor['limpa'],cor['azul'],pow(n,(1/2)),cor['limpa']))