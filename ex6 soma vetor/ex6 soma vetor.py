somaVetor = 0

tamanho = int(input("Quantos valores serão inseridos? "))

vetor = [0 for x in range(tamanho)]
for i in range (0, tamanho):
    vetor[i] = float(input("Insira um valor: "))
    somaVetor += vetor[i]

print(f"Valores inseridos no vetor: ", end = "")
for i in range (0, tamanho):
    print(f"{vetor[i]:.1f} ", end = "")

print(f"\nSoma dos valores inseridos: {somaVetor}")
print(f"Média dos valores inseridos: {somaVetor / tamanho}")
