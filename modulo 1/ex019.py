import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
alunos =[a1,a2,a3]
sorte = random.choice(alunos)
print('O aluno sorteado é {}'.format(sorte))
