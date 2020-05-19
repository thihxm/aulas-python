-- Table: contatos
CREATE TABLE contatos (
codContato INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(100) NOT NULL,
foneCelular VARCHAR(20),
limiteCredito INTEGER
);

INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (1, 'Janis Joplin', '(41) 9 9999-9999', 500);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (2, 'Jimi Hendrix', '(41) 9 8888-7777', 700);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (3, 'Dolores O Riordan', '(41) 9 7777-7777', 900);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (4, 'Malcolm Young', '(41) 9 6666-7777', 1300);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (5, 'Kid Vinil', '(41) 9 6666-6666', 1700);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (6, 'Chris Cornell', '(41) 9 6666-5555', 2000);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (7, 'George Michael', '(41) 9 6666-4444', 2300);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (8, 'Prince', '(41) 9 6666-3333', 2500);
INSERT INTO contatos (codContato, nome, foneCelular, limiteCredito) VALUES (9, 'Lemmy Kilmister', '(41) 9 2222-7777', 7000);

-- Table: emailsContatos
CREATE TABLE emailsContatos (
codEmail INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
codContato INTEGER NOT NULL,
email VARCHAR(100) NOT NULL,

FOREIGN KEY (codContato) REFERENCES contatos (codContato)
);

INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (1, 1, 'janis@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (2, 2, 'jimi@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (3, 3, 'dolores@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (4, 4, 'm.young@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (5, 5, 'kid@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (6, 6, 'cornell@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (7, 7, 'george@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (8, 8, 'prince@heaven.com');
INSERT INTO emailsContatos (codEmail, codContato, email) VALUES (9, 9, 'l.kilmister@heaven.com');
