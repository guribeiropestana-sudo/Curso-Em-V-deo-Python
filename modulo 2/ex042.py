n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2< n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos, FORMAM UM TRIANGULO',end=' ')
    if n1 == n2 == n3:
        print('EQUILÁTERO.')
    if n1 != n2 != n3 != n1:
        print('ESCALENO.')
    else:
        print('ISOCELES.')
else:
    print('esses segmentos não formam um triângulo')





a = int(input('1° Lado: '))
b = int(input('2° Lado: '))
c = int(input('3° Lado: '))
if a + b > c and a + c > b and b + c > a:
    print('Isso forma um triângulo')
    if a == b and b == c and c == a:
        print('Forma um equilatero')
    elif a != b and b != c and a != c:
        print('Forma um escaleno')