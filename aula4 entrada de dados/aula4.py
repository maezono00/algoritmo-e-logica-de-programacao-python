#nome: str
#idade: int
#salario: float
#sexo: str

nome = input("Insira nome: ")
sexo = input("Insira sexo: ")
idade = int(input("Insira sua idade: "))
salario = float(input("Insira seu salário: "))

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Idade: {idade} anos")
print(f"Salário: R${salario:.2f}")