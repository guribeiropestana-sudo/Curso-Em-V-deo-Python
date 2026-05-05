from time import sleep
from random import randint
while True:
    print('\033[1;35mJOKÊNPO CONTRA A MÁQUINA!\033[m')
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = randint(0,2)
    print("""SUAS OPÇÕES
[0] \033[4;37mPEDRA\033[m
[1] \033[4;35mPAPEL\033[m
[2] \033[4;31mTESOURA\033[m""")
    jogador = int(input('Qual é a sua jogada? '))
    print('\033[35mJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO\033[m')
    print('-='*10)
    print('O computador escolheu {}'.format(itens[computador]))
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('-='*10)
    if computador == 0:#computador PEDRA
        if jogador == 0:
            print('\033[34mEMPATE\033[m')
        elif jogador == 1:
            print('\033[32mJOGADOR VENCE\033[m')
        elif jogador == 2:
            print('\033[31mCOMPUTADOR VENCE\033[m')
    elif computador == 1:#computador PAPEL
        if jogador == 0:
            print('\033[31mCOMPUTADOR VENCE\033[m')
        if jogador == 1:
            print('\033[34mEMPATE\033[m')
        if jogador == 2:
            print('\033[32mJOGADOR VENCE\033[m')
    elif computador == 2: #computador tesoura
        if jogador == 0:
            print('\033[32mJOGADOR VENCE\033[m')
        if jogador == 1:
            print('\033[31mCOMPUTADOR VENCE\033[m')
        if jogador == 2:
            print('\033[34mEMPATE\033[m')
    
    con = str(input('Deseja jogar novamente? [S/N]'))
    if con in 'nN':
        break
print('\033[1;36mOBRIGADO POR JOGAR!!')