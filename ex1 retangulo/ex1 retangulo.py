import math

base = float(input("Insira a base do retângulo: "))
altura = float(input("Insira a altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"A área do retângulo é: {area:.4f}")
print(f"O perímetro do retângulo é: {perimetro:.4f}")
print(f"A diagonal do retângulo é: {diagonal:.4f}")