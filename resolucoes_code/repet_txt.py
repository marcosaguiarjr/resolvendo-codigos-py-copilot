#Quero inserir uma palavra e depois a quantidade de vezes que quero repeti-la.
palavra = input("Digite uma palavra: ")
while True:
    try:
        quantidade = int(input("Digite a quantidade de vezes que deseja repetir a palavra: "))
        if quantidade < 0:
            print("Por favor, digite um número inteiro não negativo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

resultado = (" " + palavra) * quantidade
print("Resultado:", resultado)