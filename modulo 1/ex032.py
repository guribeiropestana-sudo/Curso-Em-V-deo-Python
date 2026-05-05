from datetime import date
from time import sleep
a = int(input('Em qual ano você está?\nColoque 0 caso queira saber o ano atual!!'))
print('CARREGANDO O ANO 🤓')
sleep(2)
if a == 0:
    print('O ano atual é {}'.format(date.today().year))
if a % 4 == 0 and a % 100 != 0 or a % 400 ==0:
    print('Esse ano é bissexto')
else:
    print('Esse não é um ano bissexto')

