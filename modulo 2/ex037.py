print('\033[31mSISTEMA DE CONVERSÃO EM BINÁRIO, OCTAL E HEXADECIMAL\033[m')
numero = int (input('Digite um valor: '))
print("""ESCOLHA UM DOS VALORES PARA CONVERSÃO.
[1] Binário
[2] Octal
[3] Hexadecimal""")
respota = int(input('Sua opção:'))
if respota == 1:
    print('{} a conversão para binário é {}'.format(numero,bin(numero)[2:]))
elif respota == 2:
    print('{} a comversão para octal é {}'.format(numero,oct(numero)[2:]))
elif respota == 3:
    print('{} a conversão para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tenta novamente.')
