num1 = float(input("Digite um numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

def media(num1, num2, num3):
    resultado = (num1 + num2 + num3) / 3
    return round(resultado,2)

print(media(num1, num2, num3))