ordemMatriz = int(input("Insira qual será a ordem da matriz: "))
somaNegativos = 0

matriz = [[0 for x in range(ordemMatriz)] for x in range(ordemMatriz)]

for i in range(0, ordemMatriz):
    for j in range(0, ordemMatriz):
        matriz[i][j] = int(input(f"Insira o valor da célula ({i}, {j}): "))
        
        #CONTAGEM DE QUANTOS NÚMEROS NEGATIVOS EXISTEM
        if matriz[i][j] < 0:
            somaNegativos += 1

for i in range(0, ordemMatriz):
    for j in range(0, ordemMatriz):
        print(f"{matriz[i][j]} ", end = "")
    print()

print(f"Diagonal principal: ", end = "")
for i in range(0, ordemMatriz):
    for j in range(0, ordemMatriz):
        if i == j:
            print(f"{matriz[i][j]} ", end = "")

print(f"\nSoma dos negativos da matriz: {somaNegativos}")

