menorNumero = 99999

for i in range(0,3):
    valor = int(input(f"Digite o valor {i + 1}: "))
    if valor < menorNumero: menorNumero = valor

print(f"O menor número é: {menorNumero}")