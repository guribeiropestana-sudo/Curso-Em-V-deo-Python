import random
from time import sleep
from colorama import Fore
n = random.randint(0,5)
print('\033[30m-=-'*17,'\033[m')
print(Fore.WHITE+'ESSE É O JOGO DE ADIVINHAR, ESCOLHA ENTRE 0 E 5!!!')
print('\033[30m-=-'*17,'\033[m')
joga = int(input(Fore.GREEN+'QUAL NÚMERO VOCÊ VAI ESCOLHER??? '))
print(Fore.BLUE+'PROCESSANDO...')
sleep(2)
if joga == n:
    print(Fore.RED+'AAAH NÂOOO, VOCÊ GANHOU DE MIM!!!🤬\nPARABENS 🤩')
else:
    print(Fore.YELLOW+'Você perdeu... que pena, o número era {}'.format(n))