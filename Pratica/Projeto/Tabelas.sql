-- -----------------------------------------------------
-- Table usuarios
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  usuario VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL,
  nome VARCHAR(255) NULL,
  telefone VARCHAR(255) NULL,
  endereco VARCHAR(255) NULL,
  tipo INTEGER NOT NULL DEFAULT 0
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
    REFERENCES usuarios (id)
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
    REFERENCES usuarios (id)
  FOREIGN KEY (idservico)
    REFERENCES servicos (id)
);


INSERT INTO usuarios (id, nome, telefone, endereco, usuario, senha, tipo) VALUES (1, 'Vinicius Renato Calebe Martins', '41 999999999', 'Rua Domingos Nascimento, 399', 'vinicius', '123456', 0);
INSERT INTO usuarios (id, nome, telefone, endereco, usuario, senha, tipo) VALUES (2, 'Victor Heitor Levi Nunes', '41 999166655', 'Rua Bôrtolo Gusso, 626', 'victor', 'senha', 0);
INSERT INTO usuarios (id, nome, telefone, endereco, usuario, senha, tipo) VALUES (3, 'Super Empresa', '41 39940784', 'Rua Pedro Wobeto, 747', 'super.empresa', 'senhasegura', 1);
INSERT INTO usuarios (id, nome, telefone, endereco, usuario, senha, tipo) VALUES (4, 'Felipe Augusto Moreira', '41 36309111', 'Rua José Braz Gomes, 719', 'felipe', 'felipe', 1);
INSERT INTO servicos (id, nome, descricao, preco, idprestador) VALUES (1, 'Instalação de Gesso', 'Instalação de gesso feita de forma rápida e segura! Utilizamos técnicas milenares chinesas de instalação de gesso, afim de garantir o melhor serviço da galáxia!', '89,10', 3);
INSERT INTO servicos (id, nome, descricao, preco, idprestador) VALUES (2, 'Desentortador de Vidros', 'Super desentortador de vidros treinado na Alemanha com as maiores e melhores técnicas disponíveis no mercado nacional e internacional. Serviço rápido e confiável', '987,99', 3);
INSERT INTO servicos (id, nome, descricao, preco, idprestador) VALUES (3, 'Conserto de Janela', 'Descrição do serviço. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed nibh purus. Curabitur eu gravida urna. Sed eleifend tempus libero, vel rutrum purus placerat non', '256,50', 4);
INSERT INTO pedidos (id, idcliente, aceito, idservico) VALUES (1, 1, 0, 1);
INSERT INTO pedidos (id, idcliente, aceito, idservico) VALUES (2, 1, 0, 3);
INSERT INTO pedidos (id, idcliente, aceito, idservico) VALUES (3, 1, 0, 2);
