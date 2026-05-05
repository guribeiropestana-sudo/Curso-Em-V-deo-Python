media = soma = qt = maior = menor= 0
r = 'S'
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    qt += 1
    if qt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor =n
    r = input('Quer continuar? [S/N] ').upper().strip()[0]
print(f'Você digitou {qt} números e a média é {soma / qt:.2f}')
print(f'O maior número: {maior}\nO menor número:{menor}\nFim')