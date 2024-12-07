import mysql.connector
from datetime import datetime
 
class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",    
            port=3306,            
            user="root",    
            password="1234",  
            database="loja" 
        )
        self.cursor = self.conexao.cursor()
        print("Conexão com o banco de dados estabelecida!")
        self.criar_tabelas()
 
    def criar_tabelas(self):
        comando_criar_produtos = """
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                descricao TEXT,
                quantidade INT NOT NULL,
                preco DECIMAL(10, 2) NOT NULL
            )
        """
        self.cursor.execute(comando_criar_produtos)
 
        comando_criar_vendas = """
            CREATE TABLE IF NOT EXISTS vendas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                produto_id INT,
                quantidade INT NOT NULL,
                data_venda DATETIME NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
        """
        self.cursor.execute(comando_criar_vendas)
        self.conexao.commit()
        print("Tabelas criadas/verificadas com sucesso!")
 
class Produto:
    def __init__(self, nome, descricao, quantidade, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
 
class Venda:
    def __init__(self, produto_id, quantidade):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data_venda = datetime.now()
 
class SistemaVendas:
    def __init__(self):
        self.bd = BancoDeDados()
 
    def adicionar_produto(self, produto):
        if not produto.nome or produto.quantidade < 0 or produto.preco <= 0:
            print("Dados do produto inválidos!")
            print("O nome não pode estar vazio, a quantidade não pode ser negativa e o preço deve ser maior que zero.")
            return None
 
        comando = """
            INSERT INTO produtos (nome, descricao, quantidade, preco)
            VALUES (%s, %s, %s, %s)
        """
        dados = (produto.nome, produto.descricao, produto.quantidade, produto.preco)
 
        self.bd.cursor.execute(comando, dados)
        self.bd.conexao.commit()
 
        novo_id = self.bd.cursor.lastrowid
        print(f"Produto '{produto.nome}' adicionado com sucesso!")
        return novo_id
 
    def buscar_produto(self, produto_id):
        self.bd.cursor.execute("SELECT * FROM produtos WHERE id = %s", (produto_id,))
        produto = self.bd.cursor.fetchone()
 
        if produto:
            return Produto(
                id=produto[0],
                nome=produto[1],
                descricao=produto[2],
                quantidade=produto[3],
                preco=produto[4]
            )
 
        print(f"Produto com ID {produto_id} não encontrado!")
        return None
 
    def listar_produtos(self):
        self.bd.cursor.execute("SELECT * FROM produtos")
        produtos = []
 
        for produto in self.bd.cursor.fetchall():
            produtos.append(Produto(
                id=produto[0],
                nome=produto[1],
                descricao=produto[2],
                quantidade=produto[3],
                preco=produto[4]
            ))
 
        if not produtos:
            print("Nenhum produto cadastrado!")
 
        return produtos
 
    def registrar_venda(self, venda):
        produto = self.buscar_produto(venda.produto_id)
 
        if not produto:
            print("Produto não encontrado!")
            return False
 
        if produto.quantidade < venda.quantidade:
            print(f"Quantidade insuficiente! Disponível: {produto.quantidade}")
            return False
 
        nova_quantidade = produto.quantidade - venda.quantidade
        self.bd.cursor.execute(
            "UPDATE produtos SET quantidade = %s WHERE id = %s",
            (nova_quantidade, venda.produto_id)
        )
 
        self.bd.cursor.execute(
            "INSERT INTO vendas (produto_id, quantidade, data_venda) VALUES (%s, %s, %s)",
            (venda.produto_id, venda.quantidade, venda.data_venda)
        )
 
        self.bd.conexao.commit()
        print(f"Venda de {venda.quantidade} unidades registrada com sucesso!")
        return True
 
 
sistema = SistemaVendas()

while True:
    print("\nMENU DO SISTEMA")
    print("1 - Adicionar novo produto")
    print("2 - Listar produtos")
    print("3 - Registrar venda")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nADICIONAR PRODUTO")
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        produto = Produto(nome, descricao, quantidade, preco)
        sistema.adicionar_produto(produto)

    elif opcao == "2":
        print("\nPRODUTOS CADASTRADOS")
        produtos = sistema.listar_produtos()
        for produto in produtos:
            print(f"\nID: {produto.id}")
            print(f"Nome: {produto.nome}")
            print(f"Descrição: {produto.descricao}")
            print(f"Quantidade: {produto.quantidade}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print("---------------------")

    elif opcao == "3":
        print("\nREGISTRAR VENDA")
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade: "))

        venda = Venda(produto_id, quantidade)
        sistema.registrar_venda(venda)

    elif opcao == "4":
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
