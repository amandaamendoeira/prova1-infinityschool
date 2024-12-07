class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular  
        self._saldo = saldo_inicial  
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self._titular}: R${self._saldo:.2f}")


print("Bem-vindo ao sistema de contas bancárias!")

nome_titular = input("Digite o nome do titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta (use 0 se não houver): "))
conta = ContaBancaria(nome_titular, saldo_inicial)

while True:
    print("\n--- Menu ---")
    print("1. Exibir saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conta.exibir_saldo()
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor_deposito)
    elif opcao == "3":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor_saque)
    elif opcao == "4":
        print("Obrigado por usar o sistema de contas bancárias!")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
