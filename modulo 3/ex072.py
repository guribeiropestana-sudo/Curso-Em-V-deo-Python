contagem = ('zero','um','dois','três','quatro','cinco',
            'seis','sete','oito','nove','dez','onze','doze',
            'treze','quatorze','quinze','desseseis','dezessete','dezoito',
            'dezenove','vinte')
while True:
    x = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= x <= 20:
        break
    print('Tente novamente. ', end='')
print(f'o número que você digitou foi {contagem[x]}')