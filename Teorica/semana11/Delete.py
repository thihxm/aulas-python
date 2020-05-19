import sqlite3


class RemoveDados(object):
    def remover(self, id):
        conn = sqlite3.connect('agenda.db')
        cursor = conn.cursor()

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



removeDados = RemoveDados()
idExcluir = int(input('Digite o id do contato para excluir: '))
removerDados.remover(idExcluir)
