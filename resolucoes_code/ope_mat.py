# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
import sys

#Ao digitar uma letra ou símbolo inválido, o programa deve avisar o usuário e pedir a entrada novamente.
def input_float(prompt):
    while True:
        try:
            s = input(prompt).strip()
            s = s.replace(',', '.')
            return float(s)
        except ValueError:
            print("Entrada inválida. Por favor digite um número (use ',' ou '.' como separador decimal).")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada pelo usuário. Encerrando.")
            sys.exit(1)

# Nova função que valida a operação desejada
def input_operation(prompt):
    valid = {
        '+': 'soma', 'soma': 'soma', 'somar': 'soma',
        '-': 'subtracao', 'subtracao': 'subtracao', 'subtrair': 'subtracao',
        '*': 'multiplicacao', 'x': 'multiplicacao', '×': 'multiplicacao', 'multiplicacao': 'multiplicacao', 'multiplicar': 'multiplicacao',
        '/': 'divisao', 'divisao': 'divisao', 'dividir': 'divisao'
    }
    while True:
        try:
            op = input(prompt).strip().lower()
            op = op.replace('ç', 'c')  # aceitar 'subtração' sem cedilha
            if op in valid:
                return valid[op]
            print("Operação inválida. Escolha entre: soma (+), subtracao (-), multiplicacao (* ou x), divisao (/).")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada pelo usuário. Encerrando.")
            sys.exit(1)

num1 = input_float("Digite o primeiro número: ")
num2 = input_float("Digite o segundo número: ")

# pedir operação ao usuário
operacao = input_operation("Escolha a operação (soma, subtracao, multiplicacao, divisao ou + - * /): ")

# tratar divisão por zero
if operacao == 'divisao':
    while abs(num2) < 1e-12:
        print("Divisão por zero não é permitida.")
        num2 = input_float("Digite um divisor diferente de zero: ")

# executar operação
if operacao == 'soma':
    resultado = num1 + num2
    simbolo = '+'
elif operacao == 'subtracao':
    resultado = num1 - num2
    simbolo = '-'
elif operacao == 'multiplicacao':
    resultado = num1 * num2
    simbolo = '*'
elif operacao == 'divisao':
    resultado = num1 / num2
    simbolo = '/'

print(f"{num1} {simbolo} {num2} = {resultado}")