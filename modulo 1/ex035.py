
from colorama.ansi import AnsiCursor

print('=-'*20)
print('Analisador de Triângulo')
print('=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3+ r1 and r3 < r2 + r1:
    print('Seus segmentos formam um triângulo!')
else:
    print('Seus segmentos não formam um triângulo')
