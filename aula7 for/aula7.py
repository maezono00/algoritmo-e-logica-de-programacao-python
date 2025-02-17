i = 0
somaNum = 0

numeros = int(input("Quantos números serão inseridos? "))

for i in range(0, numeros):
    numero = int(input("Insira um número: "))
    somaNum += numero

print(f"A soma dos números inseridos é: {somaNum}")