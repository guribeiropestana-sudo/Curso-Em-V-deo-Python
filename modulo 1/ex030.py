from colorama import Fore
num = int(input(Fore.CYAN+'Digite um número.'))
if (num%2)==0:
    print(Fore.GREEN+'O número {} é par '.format(num))
else:
    print(Fore.BLUE+'O número {} é impar'.format(num))
print('Fim!')