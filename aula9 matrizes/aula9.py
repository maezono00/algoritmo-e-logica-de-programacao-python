linhas = int(input("Insira o número de linhas: "))
colunas = int(input("Insira o número de colunas: "))

matriz: [int] = [[0 for x in range(colunas)] for x in range(linhas)]
somaLinha: [int] = [0 for x in range(linhas)]

for i in range(0, linhas):
    for j in range(0, colunas):
        matriz[i][j] = int(input(f"Insira um valor para o elemento[{i + 1}, {j + 1}]: "))
        somaLinha[i] += matriz[i][j]

print("Matriz digitada: ")
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f"Elemento[{i + 1}, {j + 1}]: {matriz[i][j]}")

for i in range(0, linhas):
    print(f"Soma dos valores inseridos na linha {i + 1}: {somaLinha[i]}")