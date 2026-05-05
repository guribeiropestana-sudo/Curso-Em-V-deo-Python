from random import randint
print('JOGO DE ADIVINHA')
cont = 0
computador = randint(0,10)
jogador = int(input('Digite um valor entre 0 e 10: '))
while jogador != computador:
    jogador = int(input('Você digitou um número diferente, pense em outro: '))
    cont +=1
print('O jogador acertou o número.')
print('\nComputador: {}\nJogador: {}\nForam necessárias: {} tentativas'.format(computador,jogador,cont))

from random import randint
print('JOGO DE ADIVINHA')
jogador = int(input('Escolha um número 1 e 10: '))
computador = randint(1,10)
x = 0
while computador != jogador:
    jogador = int(input('Você errou, tente outro: '))
    x += 1
print('Você acertou!')
print(f'Número do Jogador: {jogador}\nNúmero do Computador: {computador}\nTentativas realizadas: {x}')