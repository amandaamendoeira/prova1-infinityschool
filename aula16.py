
CREATE DATABASE Estoque;

USE Estoque;

CREATE TABLE Produtos (
    ProdutoID INT AUTO_INCREMENT PRIMARY KEY,
    NomeProduto VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10, 2)
);

INSERT INTO Produtos (NomeProduto, Quantidade, Preco)
VALUES 
    ('Produto A', 100, 25.50),
    ('Produto B', 200, 15.75),
    ('Produto C', 150, 45.00);
