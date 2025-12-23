#calcular a média de três notas fornecidas pelo usuário
notas = []
for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")