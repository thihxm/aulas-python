-- -----------------------------------------------------
-- Table clientes
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS clientes (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(255) NULL,
  telefone VARCHAR(255) NULL,
  endereco VARCHAR(255) NULL,
  usuario VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL
);


-- -----------------------------------------------------
-- Table prestadores
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prestadores (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(255) NULL,
  telefone VARCHAR(255) NULL,
  endereco VARCHAR(255) NULL,
  usuario VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL
);


-- -----------------------------------------------------
-- Table servicos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS servicos (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(255) NULL,
  descricao VARCHAR(255) NULL,
  preco VARCHAR(45) NULL,
  idprestador INTEGER NULL,
  FOREIGN KEY (idprestador)
    REFERENCES prestadores (id)
);


-- -----------------------------------------------------
-- Table pedidos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS pedidos (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  idcliente INTEGER NOT NULL,
  aceito BOOLEAN NOT NULL DEFAULT 0,
  idservico INTEGER NOT NULL,
  FOREIGN KEY (idcliente)
    REFERENCES clientes (id)
  FOREIGN KEY (idservico)
    REFERENCES servicos (id)
);
