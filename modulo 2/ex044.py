valor = float(input('Preço da compra: R$'))
print("""Formas de pagar
[1] Cartão ou Cheque
[2] à vista no cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão""")
forma = int(input('Qual é a forma de pagamento? '))
if forma == 1:
    m = valor*(10/100)
    print('Você vai pagar {}, com 10% desconto.'.format(valor - m))
elif forma == 2:
    n = valor*(5/100)
    print('Você vai pagar {}, com 5% desconto'.format(valor - n))
elif forma == 3:
    print('O preço é normal, mesmo valor a ser pago')
elif forma == 4:
    parcelas = int(input('Em quantas parcelas? '))
    juros = valor * 20/100
    por = (valor + juros) / parcelas
    print('Sua compra será parcelada em {}x de {:.2f}R$ com juros'.format(parcelas, por))
    print('Sua compra de {}R$, irá custar {:.2f}R$'.format(valor, valor+juros))

pr = float(input('Valor do produto: R$'))
print("""Forma de pagamento
[1] Dinheiro ou cheque (10% de desconto)
[2] Cartão (5% de desconto)
[3] 2x Cartão (Preço normal)
[4] 3x Cartão (20% de juros)""")
x = int(input(''))
if x == 1:
    print('Valor do produto: R${:.2f}\n Preço a pagar: R${:.2f}'.format(pr,pr-(pr*0.10)))
elif x == 2:
    print('Valor do produto: R${:.2f}\n Preço a pagar: R${:.2f}'.format(pr, pr-(pr*0.05)))
elif x == 3:
    print('Valor do produto: R${:.2f}\n Preço igual.'.format(pr))
elif x == 4:
    par = int(input('Quantas parcelas: '))
    juros = (pr*0.20)
    print(' Parcelas: {}\n Preço da parcela: {:.2f}'.format(par,(pr+juros)/par))
    print(' Preço do produto: R${}\n Preço com juros: R${:.2f}'.format(pr,pr+(pr*0.20)))

