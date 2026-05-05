print('\033[34mCALCULADORA IMC\033[m')
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso/(pow(altura,2))
print('Seu IMC é {:.1f}'.format(imc))
if imc <=18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <=25:
    print('PESO IDEAL')
elif 25 <= imc <= 30:
    print('SOBREPESO')
elif 30 <= imc <=40:
    print('OBESIDADE')
else:
    print('Você está com um IMC maior que 40\nSeu estado:OBESIDADE MÓRBIDA')


p = float(input('Peso: '))
a = float(input('Altura: '))
imc = p / (pow(a,2))
if imc <= 18.5:
    print(f'Abaixo do peso\nIMC: {imc:.1f}')
elif 18.5 <= imc <= 25:
    print(f'Peso ideal\nIMC: {imc:.1f}')
elif 25 <= imc <= 30:
    print(f'Sobrepeso\nIMC: {imc:.1f}')
elif 30 <= imc <= 40:
    print(f'Obesidade\nIMC: {imc:.1f}')
elif 40 <= imc:
    print(f'Obesidade Morbida\nIMC: {imc:.1f}')