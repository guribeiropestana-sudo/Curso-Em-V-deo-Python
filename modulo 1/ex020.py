import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
al = [a1,a2,a3,a4]
lista = (random.sample
         (al,4))
print('A lista escolhidos é {}'.format(lista))
