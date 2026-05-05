from time import sleep
from colorama import Fore
print(Fore.BLACK+'-=-'*15)
print(Fore.WHITE+'DESCOBRINDO VALOR DO ÂNGULO SUPLEMENTAR!!!')
print(Fore.BLACK+'-=-'*15)
an = int(input(Fore.CYAN+'Fale um ângulo, que irei te dar o valor do outro '))
x = 180 - an
print(Fore.BLUE+'Processando...')
sleep(2)
print('O valor do outro ângulo é {}°'.format(x))
print(Fore.MAGENTA+'PRONTINHOOOOOOO\nCHEGAMOS NO RESULTADOOOOOOO!!!')
