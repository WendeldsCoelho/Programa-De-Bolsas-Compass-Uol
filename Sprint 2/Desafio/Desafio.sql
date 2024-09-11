-- Para normalizar eu removi os grupos repetitivos  e olhei se todos os campos tinha apenas um valor no registro

-- Após, eu garanti que todos os atributos não chave dependiam da chave priária forma completa

-- Subdividi os dados da tabela tb_locacao e removi dependências dos atributos não chave em relação a outros atributos que não seja sua chave primária

CREATE TABLE Combustivel AS 
SELECT DISTINCT 
    idcombustivel,
    tipoCombustivel
FROM tb_locacao;

-- Criação da tabela Carro 
CREATE TABLE Carro (
    idCarro INT,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    codCombustivel INT,
    FOREIGN KEY (codCombustivel) REFERENCES Combustivel(idcombustivel)
);

-- preenchendo a tabela Carro com os dados de tb_locacao
INSERT INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, codCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel AS idcombustivel
FROM tb_locacao;

-- Criação da tabela Cliente
CREATE TABLE Cliente (
    idCliente INT,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40),
    CodCarro INT,
    FOREIGN KEY (CodCarro) REFERENCES Carro(idCarro)
);

-- preenchendo a tabela Cliente com os dados de tb_locacao
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente, CodCarro)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente, idCarro
FROM tb_locacao;

-- Criação da tabela Vendedor
CREATE TABLE Vendedor (
    idVendedor INT,
    nomeVendedor VARCHAR(15),
    sexoVendedor VARCHAR(15),
    estadoVendedor VARCHAR(40),
    CodCliente INT,
    FOREIGN KEY (CodCliente) REFERENCES Cliente(idCliente)
);

-- preenchendo a tabela Cliente com os dados de tb_locacao
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor, CodCliente)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor, idCliente
FROM tb_locacao;

-- Criação da tabela Locao
CREATE TABLE Locacao (
    idLocacao INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    CodVendedor INT,
    FOREIGN KEY (CodVendedor) REFERENCES Vendedor(idVendedor)
);

-- preenchendo a tabela Locacao com os dados de tb_locacao
INSERT INTO Locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, CodVendedor)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;

-- Consultas modelo relacional
-- ----------------
SELECT * FROM  Combustivel;
SELECT * FROM Carro;
SELECT * FROM Cliente;
SELECT * FROM Vendedor;
SELECT * FROM Locacao;



-- Criando o DW
-------------------
-- Dimensão Vendedor
CREATE VIEW dim_Vendedor AS
SELECT 
    idVendedor AS idVendedor,
    nomeVendedor AS nomeVendedor,
    sexoVendedor AS sexoVendedor,
    estadoVendedor AS estadoVendedor
FROM Vendedor;

-- Dimensão Cliente
CREATE VIEW dim_Cliente AS
SELECT DISTINCT 
    idCliente AS idCliente,
    nomeCliente AS nomeCliente,
    cidadeCliente AS cidadeCliente,
    estadoCliente AS estadoCliente,
    paisCliente AS paisCliente
FROM Cliente;
-- Dimensão Carro
CREATE VIEW dim_Carro AS
SELECT  
	idCarro AS idCarro,
	kmCarro AS kmCarro,
	classiCarro AS classiCarro,
	marcaCarro AS marcaCarro,
	modeloCarro AS modeloCarro,
	anoCarro AS anoCarro,
	codCombustivel AS codCombustivel,
	tipoCombustivel AS tipoCombustivel
FROM Carro  AS ca
JOIN Combustivel co on ca.codCombustivel = co.idcombustivel;

-- Dimensão Data
CREATE VIEW dim_Data AS
SELECT DISTINCT 
    dataLocacao as dataLocacao,
    dataEntrega as dataEntrega,
    horaLocacao as horaLocacao,
    horaEntrega as horaLocacao
FROM Locacao;

-- Fato Locacao
CREATE VIEW fato_Locacao AS
SELECT
    Locacao.idLocacao,
    Locacao.dataLocacao,
    Locacao.qtdDiaria,
    Locacao.vlrDiaria,
    Locacao.codVendedor,
    Cliente.idCliente AS codCliente,
    Carro.idCarro AS codCarro
FROM
    Locacao
JOIN
    Vendedor ON Locacao.CodVendedor = Vendedor.idVendedor
JOIN
    Cliente ON Vendedor.CodCliente = Cliente.idCliente
JOIN
    Carro ON Cliente.CodCarro = Carro.idCarro;
  
-- Consultados ao DW
----------------------
SELECT * FROM dim_Vendedor;
SELECT * FROM dim_Cliente;
SELECT * FROM dim_Carro;
SELECT * FROM dim_Data;
SELECT * FROM fato_Locacao;
