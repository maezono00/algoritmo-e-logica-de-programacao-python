nome1 = str(input("Insira o nome da primeira pessoa: "))
idade1 = int(input("Insira a idade da primeira pessoa: "))
nome2 = str(input("Insira o nome da segunda pessoa: "))
idade2 = int(input("Insira a idade da segunda pessoa: "))

print("Dados da primeira pessoa: ")
print(f"Nome: {nome1}")
print(f"Idade: {idade1}")
print("Dados da segunda pessoa: ")
print(f"Nome: {nome2}")
print(f"Idade: {idade2}")
print(f"A média das idades entre {nome1} e {nome2} é de {(idade1 + idade2) / 2:.0f} anos.")