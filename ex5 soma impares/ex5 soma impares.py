menorValor = 999999
maiorValor = 0
somaImpares = 0

valor1 = int(input("Insira um valor: "))
valor2 = int(input("Insira outro valor: "))

if valor1 < menorValor: menorValor = valor1
if valor2 < menorValor: menorValor = valor2
#print(f"Menor valor: {menorValor}")

if valor1 > maiorValor: maiorValor = valor1
if valor2 > maiorValor: maiorValor = valor2
#print(f"Maior valor: {maiorValor}")

for i in range(menorValor, maiorValor):
    if i % 2 != 0:
        somaImpares += i

print(f"A soma dos ímpares é: {somaImpares}")