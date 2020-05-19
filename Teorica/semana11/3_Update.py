import sqlite3

class Contatos(object):
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

#Mostra os contatos existentes na tabela do BD
cursor.execute("""
               SELECT * FROM contatos;
               """)
print("Listagem dos registros cadastrados \n")
print("Codigo | Nome | Telefone | Email")
for registro in cursor.fetchall():
    print(registro)

conn.close()

alterarContato = Contatos(
        id = int(input('Digite o código do contato para alterar (Id): ')),
        nome = input ('Novo nome do contato: '),
        telefone = input ('Novo telefone do contato: '),
        email = input ('Novo email do contato: ')
)

# alterando os dados da tabela
conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()
cursor.execute("""
               UPDATE contatos
               SET nome = ?, telefone = ?, email = ?
               WHERE id = ? """,
               (alterarContato.nome, alterarContato.telefone, alterarContato.email, alterarContato.id)
               )

conn.commit()

print('Dados do contato atualizados com sucesso.')

conn.close()

