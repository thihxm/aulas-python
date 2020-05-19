import sqlite3

bd = 'SistemaAgenda.db'

class ConsultaDados:
       
    def listaTodosContatos(self):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT * FROM contatos;
                       """
                       )

        for i in cursor.fetchall():
            print(i)

        conn.close()

    
    def buscaParteNome(self, parteNome):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT * FROM contatos WHERE nome LIKE '%{}%' 
                """ .format(parteNome)
                )

        for registros in cursor.fetchall():
            print(registros)

        conn.close()
       
    def variasTabelas(self):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                SELECT c.nome AS NomeContato, 
                e. email AS EmailContato, 
                c.limiteCredito AS LimiteCredito
                FROM contatos c, emailsContatos e
                WHERE c.codContato = e.codContato
                ORDER BY c.limiteCredito DESC;
                """
                )
        print('Contatos com emails ordenados a partir do maior limite de crédito')
        print('Nome | E-mail | Limite de Crédito')
        for registros in cursor.fetchall():
            print(registros)

        conn.close()
    
    def contaNrContatos(self):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                SELECT COUNT (*)
                FROM contatos;
                """
                )
                
        total = cursor.fetchone()[0]
       
        print('Você possui {} contato(s) cadastrado(s) no seu sistema...'.format(total))

        conn.close()
        
    def contaNrContatosLimCred(self, valor):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute(
                """SELECT COUNT(*) FROM contatos WHERE limiteCredito > {}; """ .format(valor)
                )

        total = cursor.fetchone()[0]

        print('Você possui {0} contato(s) com limite de crédito acima de R$ {1:.2F}...'.format(total, valor))

        conn.close()
        
        
    def calculaMediaCredito(self):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                SELECT AVG (limiteCredito)
                FROM contatos;
                """
                )
                
        total = cursor.fetchone()[0]
       
        print('A média do total de crédito dos seus clientes é de R$ {:.2f}.'.format(total))

        conn.close()     
        
        
    def calculaMediaFaixaCredito(self, vlrInicial, vlrFinal):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                SELECT AVG (limiteCredito)
                FROM contatos
                WHERE limiteCredito >= {0} AND limiteCredito <= {1};
                """ .format(vlrInicial, vlrFinal)
                )
                
        total = cursor.fetchone()[0]
       
        print('A média do total de crédito dos seus clientes é de R$ {:.2f}.'.format(total))

        conn.close()         
        
    def somaLimitesCredito(self):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                SELECT SUM (limiteCredito)
                FROM contatos;
                """
                )
                
        total = cursor.fetchone()[0]
       
        print('O total de crédito acumulado (somado) dos seus clientes é de R$ {:.2f}.'.format(total))

        conn.close()             
        
    def listaLimiteCredMin(self):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                SELECT MIN (limiteCredito)
                FROM contatos;
                """
                )
                
        total = cursor.fetchone()[0]
       
        print('Valor mínimo de crédito dos seus clientes é de R$ {:.2f}.'.format(total))

        conn.close()
    
    def listaLimiteCredMax(self):
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()

        cursor.execute("""
                SELECT MAX (limiteCredito)
                FROM contatos;
                """
                )
                
        total = cursor.fetchone()[0]
       
        print('Valor máximo de crédito dos seus clientes é de R$ {:.2f}.'.format(total))

        conn.close()
        
    def limpaTela(self):
        print('\n' * 50)

    

listaDados = ConsultaDados()
listaDados.limpaTela()

#listaDados.listaTodosContatos()
#listaDados.buscaParteNome('j')
#listaDados.variasTabelas()
#listaDados.contaNrContatos()
#listaDados.contaNrContatosLimCred(2000)
#listaDados.calculaMediaCredito()
#listaDados.calculaMediaFaixaCredito(1000, 3000)
#listaDados.somaLimitesCredito()
#listaDados.listaLimiteCredMin()
#listaDados.listaLimiteCredMax()
