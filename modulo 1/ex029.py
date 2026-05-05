from colorama import Fore
v = float(input(Fore.BLUE+'Qual é a velocidade do seu veículo? KM/h'))
if v>80:
    print(Fore.RED+'Você foi multado!!\nTerá que pagar {}R$ de multa'.format((v - 80)*7.0))
else:
    print(Fore.GREEN+'Está dentro do limite!')
print('Fim.')