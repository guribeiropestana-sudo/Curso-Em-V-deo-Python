import sys
import datetime
print('\033[32mALISTAMENTO\033[m')
genero = str(input('Qual é o seu sexo? '))
if genero == 'feminino':
    print('Você não precisa se alistar.')
    sys.exit()
else:
    print('Você precisa se alistar')
ano = int(input('Qual ano você nasceu? '))
idade = 2025 - ano
print('Sua idade: {}'.format(idade))
if idade > 18:
    m = idade - 18
    p = 2025 - m
    print('Já passou o tempo do seu alistamento há {} anos'.format(m))
    print('Ano do seu alistamento: {}'.format(p))
elif idade < 18:
    n = 18 - idade
    x = 2025 + n
    print('Faltam {} anos para se alistar.'.format(n))
    print('Ano do seu alistamento: {}'.format(x))
elif idade == 18:
    print('Você deve se alitar.')