valor1 = int(input("Por favor, insira um valor: "))
valor2 = int(input("Por favor, insira outro valor: "))

while valor1 != valor2:
    if valor1 < valor2: print("Ordem Crescente!")
    else: print("Ordem Descrescente")

    valor1 = int(input("Por favor, insira um valor: "))
    valor2 = int(input("Por favor, insira outro valor: "))