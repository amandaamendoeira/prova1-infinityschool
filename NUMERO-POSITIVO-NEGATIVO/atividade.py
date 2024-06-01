numero = float(input("Digite um número: "))

if numero > 0:
    mensagem = (f"O número é positivo.")
elif numero < 0:
    mensagem = (f"O número é negativo.")
else:
    mensagem = (f"O número é zero.")

print(mensagem)