listagem = ('Lápis', 1.75,
            'Caderno', 8.00,
            'Borracha', 2.00,
            'Estojo', 20.0,
            'Transferidos',4.20,
            'Compasso', 9.99,
            'Mochila',120.0,
            'Canetas',1.0,
            'Livro',35.0)

for x in range(0, len(listagem)):
    if x %2 == 0:
        print(f'{listagem[x]:.<30}',end='')
    else:
        print(f'R${listagem[x]:.2f}')