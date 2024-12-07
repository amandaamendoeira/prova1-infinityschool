
CREATE DATABASE MeuBancoDeDados;

USE MeuBancoDeDados;

CREATE TABLE Clientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Idade INT,
    Cidade VARCHAR(100)
);
