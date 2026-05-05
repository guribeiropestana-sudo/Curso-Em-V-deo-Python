tabela = ('Flamengo','Palmeiras','Cruzeiro','Mirassol','Fluminense',
          'Botafogo','Bahia','São Paulo','Grêmio','Bragantino','Atlético-MG',
          'Santos','Corinthians','Vasco Da Gama','EC Vitória','Internacional','Ceará-SC',
          'Fortaleza','Juventude','Sport Recife')
print('Os 5 primeiros colocados são:')
for x in range (0, 5):
    print(tabela[x])
print('-='*20)
print('Os 4 últimos são: ')
for c in range (-4,0):
    print(tabela[c])
print('-=' * 20)
print(sorted(tabela))
print('-='*20)
print(f'O time do São Paulo está na {tabela.index("São Paulo")+1}° posição.')