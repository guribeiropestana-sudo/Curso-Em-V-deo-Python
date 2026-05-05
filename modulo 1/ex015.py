km = float(input('Quantos Km você rodou com o carro? Km'))
d = float (input('Quantos dias você ficou com o carro?'))
print('Total a pagar é {:.0f}R$'.format(d*60 + km*0.15))
print('Por Km = {:.0f}R$\nPor dia = {:.0f}R$'.format(km*0.15,d*60))
