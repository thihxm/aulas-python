import sqlite3

class Contatos(object):
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

novoContato = Contatos(
        nome = input ('Nome do contato: '),
        telefone = input ('Telefone do contato: '),
        email = input ('Email do contato: ')
)

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

cursor.execute("""
               INSERT INTO contatos (nome, telefone, email) 
               VALUES (?,?,?)""", 
               (novoContato.nome, novoContato.telefone, novoContato.email)
               )

conn.commit()
print('Dados inseridos com sucesso.')
conn.close()