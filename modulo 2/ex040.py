print('\033[35mBOLETIM BIMESTRAL\033[m')
m1 = float(input('Sua nota: '))
m2 = float(input('Sua nota: '))
media = (m1 + m2)/2
print('Sua média é {}'.format(media))
if media < 5:
    print('Você está reprovado')
elif media == 5 or media<=6.9:
    print('Você está de recuperação')
elif media >=7:
    print('Você foi aprovado')