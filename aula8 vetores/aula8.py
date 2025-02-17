N = int(input("Quantos números serão inseridos? "))

vetor: [float] = [0 for x in range(N)]

somaValor = 0
for i in range(0,N):
    vetor[i] = float(input("Insira um número: "))
    somaValor += vetor[i]

print("Números inseridos: ")
for i in range (0,N):
    print(f"{vetor[i]:.2f}")

print(f"A soma dos números inseridos é: {somaValor}")