n1 = float(input('Sua nota no 1° bimestre '))
n2 = float(input('Sua nota no 2° bimestre'))
cor = {'limpa':'\033[m',
       'verde':'\033[4;32m'}
print('A soma das suas notas é de {}{:.1f}{} pontos\nA média entre suas notas é de {}{:.1f}{} pontos'.format(cor['verde'],n1 + n2,cor['limpa'],cor['verde'],(n1 + n2)/2,cor['limpa']))


