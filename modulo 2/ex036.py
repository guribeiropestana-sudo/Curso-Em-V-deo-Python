print('\033[32mEMPRÉSTIMO DE UMA CASA\033[m')
c = float(input('Qual é o valor da casa que deseja comprar? R$'))
s = float(input('Qual é o valor do seu salário? R$'))
a = float(input('Quantos anos você vai pagar a sua casa? '))
m = a *12
pc = c/m
r = s*(30/100)
print('Você terá que pagar {:.2f}R$ por mês em {:.0f} meses.'.format(pc,m))
if pc>=r:
    print('\033[31mVOCÊ NÃO PODE COMPRAR ESTA CASA!\033[m')
else:
    print('\033[32mVocê pode comprar esta casa de boa!\033[m')