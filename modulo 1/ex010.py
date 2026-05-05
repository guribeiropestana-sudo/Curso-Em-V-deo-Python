d = float(input('Quanto de dinheiro em reais você tem? R$'))
print('Você pode comprar \033[33m{:.2f}\033[m dolares\nVocê pode comprar \033[32m{:.2f}\033[m euros'.format(d/3.27,d/6.21))
print('E pode comprar \033[34m{:.2f}\033[m pesos argentinos'.format(d*264.53))
