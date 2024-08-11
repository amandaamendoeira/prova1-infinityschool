nome = input("Digite o seu nome: ")
telefone = input("Digite o seu telefone: ")
email = input("Digite o e-amil para contato: ")

contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email
}

print("\nInformações do contato: ")
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")