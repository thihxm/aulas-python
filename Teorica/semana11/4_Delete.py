import sqlite3

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

idExcluir = int(input('Digite o id do contato para excluir: '))


# excluindo um registro da tabela
cursor.execute("""
               DELETE FROM contatos
               WHERE id = ?
               """, 
               (idExcluir,)
               )

conn.commit()

print('Registro excluido com sucesso.')

conn.close()