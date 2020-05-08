CREATE TABLE contatos (
codContato INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome VARCHAR (100) NOT NULL,
foneCelular VARCHAR(20)
);

INSERT INTO contatos VALUES(NULL, 'Janis Joplin', '(41) 9 8888-8888');
INSERT INTO contatos VALUES(NULL, 'Jimi Hendrix', '(41) 9 8888-7777');
INSERT INTO contatos VALUES(NULL, 'Dolores O Riordan', '(41) 9 7777-7777');
INSERT INTO contatos VALUES(NULL, 'Malcolm Young', '(41) 9 6666-7777');
INSERT INTO contatos VALUES(NULL, 'Kid Vinil', '(41) 9 6666-6666');
INSERT INTO contatos VALUES(NULL, 'Chris Cornell', '(41) 9 6666-5555');
INSERT INTO contatos VALUES(NULL, 'George Michael', '(41) 9 6666-4444');
INSERT INTO contatos VALUES(NULL, 'Prince', '(41) 9 6666-3333');
INSERT INTO contatos VALUES(NULL, 'Lemmy Kilmister', '(41) 9 2222-7777');


CREATE TABLE emailsContatos (
codEmail INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
codContato INTEGER NOT NULL,
email VARCHAR(100) NOT NULL,
FOREIGN KEY (codContato) REFERENCES contatos(codContato)
);

INSERT INTO emailsContatos VALUES(NULL, 1, 'janis@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 1, 'janis@heavenplus.com');
INSERT INTO emailsContatos VALUES(NULL, 2, 'jimi@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 3, 'dolores@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 4, 'm.young@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 5, 'kid@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 6, 'cornell@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 7, 'george@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 8, 'prince@heaven.com');
INSERT INTO emailsContatos VALUES(NULL, 9, 'lemmyrock@heaven.com');