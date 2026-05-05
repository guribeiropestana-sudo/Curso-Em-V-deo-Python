frase = str(input('Digite uma frase ')).strip()
x = frase.upper()
print('Existe {} A na frase '.format(x.count('A')))
print('Primeira vez: {}\nUltima vez {}'.format(x.find('A')+1,x.rfind('A')+1))