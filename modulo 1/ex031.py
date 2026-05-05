from colorama import Fore
d = float(input(Fore.GREEN+'Qual a distância da viagem em kilometros '))
if d<=200:
    print(Fore.BLUE+'Sua viagem custou R${}'.format(d*0.5))
else:
    print(Fore.CYAN+'Sua viagem custou R${}'.format(d*0.45))