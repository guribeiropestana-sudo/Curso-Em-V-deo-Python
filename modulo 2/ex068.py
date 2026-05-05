from random import randint
t = c =0
while True:
    computador = randint(0, 10)
    jogador1 = int(input('Escolha seu número: '))
    tipo = ' '
    t += jogador1+computador
    while tipo not in 'IiPp':
        tipo = input('Quer par ou impar: [I/P] ')
    print(f'O computador escolheu: {computador}\nO jogador escolheu: {jogador1}\nResultado: {t}')
    if t %2 ==0:
        print('DEU PAR')
    else:
        print('Deu impar')
    if tipo in 'Pp':
        if t %2 == 0:
            print('PARABENS, VOCÊ GANHOOOUUUUU')
            c +=1
        else:
            print('AAAAHHHH NAOOO, O COMPUTADOR VENCEU')
            break
    if tipo in'Ii':
        if t %2 != 0:
            print('PARABENS, VOCÊ GANHOOOOU')
            c += 1
        else:
            print('AAAAHHH NAOOOO, O COMPUTADOR VENCEU...')
            break
if c == 0:
    print('Não venceu nenhuma do computador, que humilhante...')
else:
    print(f'GAME OVER\nVitórias do jogador: {c}')