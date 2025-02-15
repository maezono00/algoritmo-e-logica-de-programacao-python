horas = int(input("Insira que horas são: "))

if horas < 12:
    print("Bom dia!!!")
if horas > 12 and horas < 18:
    print("Boa tarde!!!")
if horas > 18:
    print("Boa noite!!!")