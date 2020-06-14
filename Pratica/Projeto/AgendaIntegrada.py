import sqlite3

class Contatos(object):
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
class BancodeDadosContatos:    
    def CadastrarContato(self, novocontato):
        conn = sqlite3.connect('agenda.db')
        cursor = conn.cursor()
        
        cursor.execute("""
                INSERT INTO contatos (id, nome, telefone, email)
                VALUES (?, ?, ?, ?)
                """,
                (novocontato.id, novocontato.nome, novocontato.telefone, novocontato.email)
                )
        
        conn.commit()
        conn.close()

    def ListarContatosPorNome(self, parteNome):
        conn = sqlite3.connect('agenda.db')
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT * 
                       FROM contatos
                       WHERE nome LIKE '%{}%'
                """ .format(parteNome)
                )
        
        listagem = list()
        for registro in cursor.fetchall():
            # (Codigo, Nome, Telefone, Email)
            contato = Contatos(registro[0], registro[1], registro[2], registro[3])
            listagem.append(contato)

        conn.close()
        return listagem
   
    def AtualizarContato(self, dadosContato):
        conn = sqlite3.connect('agenda.db')
        cursor = conn.cursor()
        cursor.execute("""
               UPDATE contatos
               SET nome = ?, telefone = ?, email = ?
               WHERE id = ? """, 
               (dadosContato.nome, dadosContato.telefone, dadosContato.email, dadosContato.id)
        )

        conn.commit()
        conn.close()


    def ExcluirContato(self, contato):
        conn = sqlite3.connect('agenda.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contatos WHERE id = ?", (str(contato.id),))
        
        conn.commit()
        conn.close()

    def BuscaContatoPorId(self, id):
        conn = sqlite3.connect('agenda.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contatos WHERE id = ?", (str(id),))
        
        registro = cursor.fetchone()
        conn.close()

        if registro != None:
            return Contatos(registro[0], registro[1], registro[2], registro[3])
        else:
            return None
