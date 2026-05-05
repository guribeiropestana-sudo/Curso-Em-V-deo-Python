frase = str(input('Frase: ')).strip().upper()
palavras= frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#for letra in range(len(junto)-1, -1, -1):
#   inverso = inverso + junto[letra]
#  print(letra)
print(inverso)
if inverso == junto:
    print('É UM PALINDROMO')
else:
    print('nao é palindromo')