create database Projeto;

use Projeto;

CREATE TABLE Produto (
	Id int primary key not null auto_increment,
    Nome VARCHAR(50),
    Preco DOUBLE,
    Descricao VARCHAR(280),
    Ativo BOOLEAN,
    fk_Funcionario_Id INTEGER
);

CREATE TABLE Caixa (
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Ativo BOOLEAN
);

CREATE TABLE Funcionario (
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(50),
    Data_de_Nascimento DATE,
    Sexo CHAR,
    CPF INT,
    Senha VARCHAR(20),
    Ativo BOOLEAN
);

CREATE TABLE Local_de_Armazenamento (
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Descricao VARCHAR(280),
    Ativo BOOLEAN
);

CREATE TABLE Fornecedora (
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(50),
    Ativo BOOLEAN,
    fk_Funcionario_Id INTEGER,
    CNPJ INTEGER
);

CREATE TABLE Cliente (
    Id INTEGER PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Pessoa_Fisica(
	fk_Cliente_Id INTEGER PRIMARY KEY,
    CPF INT,
    Nome VARCHAR(50),
    Sexo CHAR,
    Data_de_Nascimento DATE,
    Ativo BOOLEAN
);

CREATE TABLE Pessoa_Juridica(
	fk_Cliente_Id INTEGER PRIMARY KEY,
    CNPJ INTEGER,
    Nome_Fantasia VARCHAR(50)
);

CREATE TABLE Entrada_Movimentacao_Local_Contem_Lote (
    Descricao VARCHAR(280),
    fk_Funcionario_Id INTEGER,
    fk_Lote_Id INTEGER,
    fk_Local_Id INTEGER,
    Ativo BOOLEAN,
    E_entrada BOOLEAN,
    Data_da_Movimentacao DATETIME
);

CREATE TABLE Lote (
    Data_de_Validade DATE,
    Preco_de_Compra DOUBLE,
    Quantidade INTEGER,
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Ativo BOOLEAN,
    Motivo_de_Alteracao VARCHAR(280)
);

CREATE TABLE Venda (
    Quantidade INTEGER,
    Data_de_Conclusao DATETIME,
    Data_de_Abertura DATETIME,
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Ativo BOOLEAN,
    fk_Cliente_Id INTEGER,
    fk_Caixa_Id INTEGER,
    fk_Forma_De_Pagamento_Id INTEGER
);

CREATE TABLE Contato (
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Ativo BOOLEAN
);

CREATE TABLE Telefone (
    DDD INTEGER,
    Numero INTEGER,
    fk_Contato_Id INTEGER PRIMARY KEY
);

CREATE TABLE E_mail (
    Endereco VARCHAR(50),
    fk_Contato_Id INTEGER PRIMARY KEY
);

CREATE TABLE Forma_De_Pagamento (
    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Descricao VARCHAR(280),
    Ativo BOOLEAN
);

CREATE TABLE Vendedor_realiza_Venda (
    fk_Funcionario_Id INTEGER,
    fk_Venda_Id INTEGER
);

CREATE TABLE Produto_fornecido_Fornecedora (
	fk_Produto_Id INTEGER,
    fk_Fornecedora_Id INTEGER
);

CREATE TABLE Gerente_cadastra_Local (
    fk_Funcionario_Id INTEGER,
    fk_Local_Id INTEGER
);

CREATE TABLE Fornecedora_fornece_Lote (
    fk_Fornecedora_Id INTEGER,
    fk_Lote_Id INTEGER
);

CREATE TABLE Produto_esta_Lote (
    fk_Produto_Id INTEGER,
    fk_Lote_Id INTEGER
);

CREATE TABLE Gerente_Abre_Fecha_Caixa (
    fk_Funcionario_Id INTEGER,
    Dia_Hora DATETIME,
    E_Abertura BOOLEAN,
    fk_Caixa_Id INTEGER
);

CREATE TABLE Venda_contem_Produto (
    fk_Produto_Id INTEGER,
    fk_Venda_Id INTEGER
);

CREATE TABLE Funcionario_tem_Contato (
    fk_Contato_Id INTEGER,
    fk_Funcionario_Id INTEGER
);

CREATE TABLE Fornecedor_tem_Contato (
    fk_Contato_Id INTEGER,
    fk_Fornecedora_Id INTEGER
);

CREATE TABLE Cliente_tem_Contato (
    fk_Contato_Id INTEGER,
    fk_Cliente_Id INTEGER
);

ALTER TABLE Pessoa_Juridica ADD CONSTRAINT FK_Pessoa_Juridica_1
	FOREIGN KEY (fk_Cliente_Id)
    REFERENCES Cliente(Id)
    ON DELETE CASCADE;

Alter Table Pessoa_Fisica ADD CONSTRAINT FK_Pessoa_Fisica_1
	FOREIGN KEY (fk_Cliente_Id)
    REFERENCES Cliente(Id)
    ON DELETE CASCADE;
 
ALTER TABLE Produto ADD CONSTRAINT FK_Produto_1
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE CASCADE;
 
ALTER TABLE Fornecedora ADD CONSTRAINT FK_Fornecedora_2
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE CASCADE;
 
ALTER TABLE Entrada_Movimentacao_Local_Contem_Lote ADD CONSTRAINT FK_Entrada_Movimentacao_Local_Contem_Lote_1
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE CASCADE;
 
ALTER TABLE Entrada_Movimentacao_Local_Contem_Lote ADD CONSTRAINT FK_Entrada_Movimentacao_Local_Contem_Lote_2
    FOREIGN KEY (fk_Lote_id)
    REFERENCES Lote (id);
 
ALTER TABLE Entrada_Movimentacao_Local_Contem_Lote ADD CONSTRAINT FK_Entrada_Movimentacao_Local_Contem_Lote_3
    FOREIGN KEY (fk_Local_Id)
    REFERENCES Local_de_Armazenamento(Id);
 
ALTER TABLE Venda ADD CONSTRAINT FK_Venda_3
    FOREIGN KEY (fk_Cliente_Id)
    REFERENCES Cliente (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Venda ADD CONSTRAINT FK_Venda_4
    FOREIGN KEY (fk_Caixa_Id)
    REFERENCES Caixa (Id)
    ON DELETE CASCADE;
 
ALTER TABLE Venda ADD CONSTRAINT FK_Venda_5
    FOREIGN KEY (fk_Forma_De_Pagamento_Id)
    REFERENCES Forma_De_Pagamento (Id)
    ON DELETE CASCADE;
 
ALTER TABLE Telefone ADD CONSTRAINT FK_Telefone_2
    FOREIGN KEY (fk_Contato_Id)
    REFERENCES Contato (Id)
    ON DELETE CASCADE;
 
ALTER TABLE E_mail ADD CONSTRAINT FK_E_mail_2
    FOREIGN KEY (fk_Contato_Id)
    REFERENCES Contato (Id)
    ON DELETE CASCADE;
 
ALTER TABLE Vendedor_realiza_Venda ADD CONSTRAINT FK_Vendedor_realiza_Venda_1
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Vendedor_realiza_Venda ADD CONSTRAINT FK_Vendedor_realiza_Venda_2
    FOREIGN KEY (fk_Venda_Id)
    REFERENCES Venda (Id)
    ON DELETE SET NULL;
 
ALTER TABLE Produto_fornecido_Fornecedora ADD CONSTRAINT FK_Produto_fornecido_Fornecedora_1
    FOREIGN KEY (fk_Fornecedora_Id)
    REFERENCES Fornecedora (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Gerente_cadastra_Local ADD CONSTRAINT FK_Gerente_cadastra_Local_1
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Gerente_cadastra_Local ADD CONSTRAINT FK_Gerente_cadastra_Local_2
    FOREIGN KEY (fk_Local_Id)
    REFERENCES Local_de_Armazenamento(Id)
    ON DELETE SET NULL;
 
ALTER TABLE Fornecedora_fornece_Lote ADD CONSTRAINT FK_Fornecedora_fornece_Lote_1
    FOREIGN KEY (fk_Fornecedora_Id)
    REFERENCES Fornecedora (Id)
    ON DELETE SET NULL;
 
ALTER TABLE Fornecedora_fornece_Lote ADD CONSTRAINT FK_Fornecedora_fornece_Lote_2
    FOREIGN KEY (fk_Lote_id)
    REFERENCES Lote (id)
    ON DELETE SET NULL;
 
ALTER TABLE Produto_esta_Lote ADD CONSTRAINT FK_Produto_esta_Lote_1
    FOREIGN KEY (fk_Lote_id)
    REFERENCES Lote (id)
    ON DELETE SET NULL;
 
ALTER TABLE Gerente_Abre_Fecha_Caixa ADD CONSTRAINT FK_Gerente_Abre_Fecha_Caixa_1
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE SET NULL;
 
ALTER TABLE Gerente_Abre_Fecha_Caixa ADD CONSTRAINT FK_Gerente_Abre_Fecha_Caixa_2
    FOREIGN KEY (fk_Caixa_Id)
    REFERENCES Caixa (Id)
    ON DELETE SET NULL;
 
ALTER TABLE Venda_contem_Produto ADD CONSTRAINT FK_Venda_contem_Produto_1
    FOREIGN KEY (fk_Venda_Id)
    REFERENCES Venda (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Funcionario_tem_Contato ADD CONSTRAINT FK_Funcionario_tem_Contato_1
    FOREIGN KEY (fk_Contato_Id)
    REFERENCES Contato (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Funcionario_tem_Contato ADD CONSTRAINT FK_Funcionario_tem_Contato_2
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE SET NULL;
 
ALTER TABLE Fornecedor_tem_Contato ADD CONSTRAINT FK_Fornecedor_tem_Contato_1
    FOREIGN KEY (fk_Contato_Id)
    REFERENCES Contato (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Fornecedor_tem_Contato ADD CONSTRAINT FK_Fornecedor_tem_Contato_2
    FOREIGN KEY (fk_Fornecedora_Id)
    REFERENCES Fornecedora (Id)
    ON DELETE SET NULL;
 
ALTER TABLE Cliente_tem_Contato ADD CONSTRAINT FK_Cliente_tem_Contato_1
    FOREIGN KEY (fk_Contato_Id)
    REFERENCES Contato (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Cliente_tem_Contato ADD CONSTRAINT FK_Cliente_tem_Contato_2
    FOREIGN KEY (fk_Cliente_Id)
    REFERENCES Cliente (Id)
    ON DELETE SET NULL;