# Lista de tarefas
lista = []

# Função para criar uma nova tarefa
def criar_tarefa():
    tarefa = {}
    nome = input("Digite o nome da tarefa: ")
    tarefa["nome"] = nome

    descricao = input("Digite a descrição: ")
    tarefa["descrição"] = descricao

    while True:
        status = input("Digite o status da tarefa (Concluída, Pendente, etc.): ").strip().lower()
        if status in ["concluida", "pendente"]:
            tarefa["status"] = status
            break
        else:
            print("Status inválido. Por favor, digite um status válido.")

    while True:
        try:
            prioridade = int(input("Digite a prioridade de 1 a 5, sendo 1 a maior prioridade e 5 a menor: "))
            if 1 <= prioridade <= 5:
                tarefa["prioridade"] = prioridade
                break
            else:
                print("Prioridade deve estar entre 1 e 5.")
        except ValueError:
            print("Digite um número válido para a prioridade.")

    categoria = input("Digite a categoria: ")
    tarefa["categoria"] = categoria

    tarefa["concluído"] = False
    lista.append(tarefa)
    print("Tarefa criada com sucesso!")

# Função para listar as tarefas por prioridade
def listar_tarefa():
    if not lista:
        print("Nenhuma tarefa encontrada.")
        return

    lista_ordenada = sorted(lista, key=lambda x: x['prioridade'])

    for principal, tarefa in enumerate(lista_ordenada, start=1):
        status = "Concluída" if tarefa["concluído"] else "Pendente"
        print(f"Tarefa {principal}:")
        print(f"  Nome: {tarefa['nome']}")
        print(f"  Descrição: {tarefa['descrição']}")
        print(f"  Prioridade: {tarefa['prioridade']}")
        print(f"  Categoria: {tarefa['categoria']}")
        print(f"  Status: {status}")
        print()

# Função para marcar uma tarefa como concluída
def marcar_tarefa():
    listar_tarefa()
    if not lista:
        return
    try:
        tarefa_marcar = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
        if 0 <= tarefa_marcar < len(lista):
            lista[tarefa_marcar]["concluído"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Função para editar uma tarefa
def editar_tarefa():
    listar_tarefa()
    if not lista:
        return

    try:
        tarefa_editar = int(input("Digite o número da tarefa que você deseja editar: ")) - 1
        if 0 <= tarefa_editar < len(lista):
            tarefa = lista[tarefa_editar]
            print("Digite novas informações (deixe em branco para manter a informação atual):")

            nome = input(f"Nome ({tarefa['nome']}): ")
            if nome:
                tarefa['nome'] = nome

            descricao = input(f"Descrição ({tarefa['descrição']}): ")
            if descricao:
                tarefa['descrição'] = descricao

            while True:
                prioridade = input(f"Prioridade ({tarefa['prioridade']}): ")
                if prioridade == '':
                    prioridade = tarefa['prioridade']
                    break
                else:
                    try:
                        prioridade = int(prioridade)
                        if 1 <= prioridade <= 5:
                            break
                        else:
                            print("Prioridade deve estar entre 1 e 5.")
                    except ValueError:
                        print("Digite um número válido para a prioridade.")

            tarefa['prioridade'] = prioridade

            categoria = input(f"Categoria ({tarefa['categoria']}): ")
            if categoria:
                tarefa['categoria'] = categoria
            
            print("Tarefa editada com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

#Função para editar por classificação
def listar_por_status():
    status = input("Digite o status (exemplo: 'concluida' ou 'pendente'): ").strip().lower()
    tarefas_filtradas = [tarefa for tarefa in lista if tarefa["status"] == status]

    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            print(f"Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, Status: {tarefa['status']}")
    else:
        print(f"Não há tarefas com o status {status}.")

# Função para excluir uma tarefa
def excluir_tarefa():
    listar_tarefa()
    if not lista:
        return
    try:
        tarefa_excluir = int(input("Digite o número da tarefa a ser excluída: ")) - 1
        if 0 <= tarefa_excluir < len(lista):
            lista.pop(tarefa_excluir)
            print("Tarefa excluída com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Menu principal
while True:
    print("Boas vindas ao Task Manager")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas por prioridade")
    print("3 - Marcar como concluído")
    print("4 - Editar tarefa")
    print("5 - Excluir tarefa")
    print("6 - Listar por classificação: concluida ou pendente")
    print("0 - Sair")

    try:
        op = int(input("Escolha uma opção: "))
        if op == 0:
            break
        elif op == 1:
            criar_tarefa()
        elif op == 2:
            listar_tarefa()
        elif op == 3:
            marcar_tarefa()
        elif op == 4:
            editar_tarefa()
        elif op == 5:
            excluir_tarefa()
        elif op == 6:
            listar_por_status()
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")