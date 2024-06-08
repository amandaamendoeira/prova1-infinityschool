
numero_secreto = 9
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número.")
        break
    else:
        if tentativas < limite_tentativas:
            print("Errado! Tente novamente.")
        else:
            print("Errado! Você atingiu o limite de tentativas.")
else:
    print(f"Que pena! O número correto era {numero_secreto}.")