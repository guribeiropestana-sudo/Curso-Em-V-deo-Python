sal = float(input('Qual é o seu salário? '))
if sal>1250:
    a = sal *0.10
    print('Quem ganhava {}R$, passa a ganhar isso {}R$'.format(sal,a + sal))
else:
    a = sal *0.15
    print('Quem ganhava {}R$, passa a ganhar isso {}R$'.format(sal, a+sal))
