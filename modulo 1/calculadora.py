num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
operacao = input('Operador que quer usar: ')

match operacao:
    case '+':
        res = num1 + num2
    case'-':
        res = num1 - num2
    case '*':
        res = num1 * num2
    case '/':
        res = num1 / num2

print(f'Resultado é \033[35m{res}')