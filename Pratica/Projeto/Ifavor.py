import sqlite3

class Cliente(object):
    def __init__(self, id, nome, telefone, endereco, usuario, senha):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.usuario = usuario
        self.senha = senha

class Prestador(object):
    def __init__(self, id, nome, telefone, endereco, usuario, senha):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.usuario = usuario
        self.senha = senha

class Pedido(object):
    def __init__(self, id, idcliente, idservico, aceito, **kwargs):
        self.id = id
        self.idcliente = idcliente
        self.idservico = idservico
        self.aceito = aceito
        self.nome_servico = kwargs.get('nome_servico')
        self.descricao_servico = kwargs.get('descricao_servico')
        self.preco_servico = kwargs.get('preco_servico')
        self.nome_prestador = kwargs.get('nome_prestador')

class Servico(object):
    def __init__(self, id, nome, descricao, preco, idprestador, **kwargs):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.idprestador = idprestador
        self.nome_prestador = kwargs.get('nome_prestador')

class BancodeDadosClientes:
    def CadastrarCliente(self, novocliente):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO clientes (id, nome, telefone, endereco, usuario, senha)
                VALUES (?, ?, ?, ?)
                """,
                (novocliente.id, novocliente.nome, novocliente.telefone, novocliente.endereco, novocliente.usuario, novocliente.senha)
                )

        conn.commit()
        conn.close()

class BancodeDadosPrestador:
    def CadastrarPrestador(self, novoprestador):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO prestadores (id, nome, telefone, endereco, usuario, senha)
                VALUES (?, ?, ?, ?)
                """,
                (novoprestador.id, novoprestador.nome, novoprestador.telefone, novoprestador.endereco, novoprestador.usuario, novoprestador.senha)
                )

        conn.commit()
        conn.close()

class BancodeDadosPedidos:
    def SolicitarPedido(self, novopedido):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO pedidos (id, idcliente, idservico, aceito)
                VALUES (?, ?, ?, ?)
                """,
                (novopedido.id, novopedido.idcliente, novopedido.idservico, novopedido.aceito)
                )

        conn.commit()
        conn.close()

    def ListarPedidosPorNomeECliente(self, parteNome, idcliente):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT
                            pedidos.id AS id,
                            pedidos.idcliente AS idcliente,
                            pedidos.idservico AS idservico,
                            pedidos.aceito AS aceito,
                            servicos.nome AS nome_servico,
                            servicos.descricao AS descricao_servico,
                            servicos.preco AS preco_servico,
                            prestadores.nome AS nome_prestador
                       FROM pedidos
                       INNER JOIN servicos ON pedidos.idservico = servicos.id
                       INNER JOIN prestadores ON servicos.idprestador = prestadores.id
                       WHERE servicos.nome LIKE '%{}%' AND pedidos.idcliente = {}
                """ .format(parteNome, idcliente)
                )

        listagem = list()
        for registro in cursor.fetchall():
            # (id, idcliente, idservico, aceito)
            pedido = Pedido(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                nome_servico = registro[4],
                descricao_servico = registro[5],
                preco_servico = registro[6],
                nome_prestador = registro[7]
            )
            listagem.append(pedido)

        conn.close()
        return listagem

    def ListarPedidosPorNomeEPrestador(self, parteNome, idprestador):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT *
                       FROM pedidos
                       INNER JOIN servicos ON pedidos.idservico = servicos.id
                       WHERE servicos.nome LIKE '%{}%' AND servicos.idprestador = {}
                """ .format(parteNome, idprestador)
                )

        listagem = list()
        for registro in cursor.fetchall():
            # (id, idcliente, idservico, aceito)
            pedido = Pedido(registro[0], registro[1], registro[2], registro[3])
            listagem.append(pedido)

        conn.close()
        return listagem

    def ExcluirPedido(self, pedido):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pedidos WHERE id = ?", (str(pedido.id),))

        conn.commit()
        conn.close()

    def BuscaPedidoPorId(self, id):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE id = ?", (str(id),))
        cursor.execute("""
                       SELECT
                            pedidos.id AS id,
                            pedidos.idcliente AS idcliente,
                            pedidos.idservico AS idservico,
                            pedidos.aceito AS aceito,
                            servicos.nome AS nome_servico,
                            servicos.descricao AS descricao_servico,
                            servicos.preco AS preco_servico,
                            prestadores.nome AS nome_prestador
                       FROM pedidos
                       INNER JOIN servicos ON pedidos.idservico = servicos.id
                       INNER JOIN prestadores ON servicos.idprestador = prestadores.id
                       WHERE pedidos.id = {}
                """ .format(id)
                )

        registro = cursor.fetchone()
        conn.close()

        if registro != None:
            return Pedido(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                nome_servico = registro[4],
                descricao_servico = registro[5],
                preco_servico = registro[6],
                nome_prestador = registro[7]
            )
        else:
            return None

class BancodeDadosServicos:
    def CadastrarServico(self, novoservico):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO servicos (id, nome, descricao, preco, idprestador)
                VALUES (?, ?, ?, ?)
                """,
                (novoservico.id, novoservico.nome, novoservico.descricao, novoservico.preco, novoservico.idprestador)
                )

        conn.commit()
        conn.close()

    def ListarServicosPorNome(self, parteNome):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT
                            servicos.id AS id,
                            servicos.nome AS nome,
                            servicos.descricao AS descricao,
                            servicos.preco AS preco,
                            prestadores.id AS idprestador,
                            prestadores.nome AS nome_prestador
                       FROM servicos
                       INNER JOIN prestadores ON servicos.idprestador = prestadores.id
                       WHERE servicos.nome LIKE '%{}%'
                """ .format(parteNome)
                )

        listagem = list()
        for registro in cursor.fetchall():
            # (id, nome, descricao, preco, idprestador, nome_prestador)
            servico = Servico(registro[0], registro[1], registro[2], registro[3], registro[4], nome_prestador = registro[5])
            listagem.append(servico)

        conn.close()
        return listagem

    def ListarServicosPorNomeEPrestador(self, parteNome, idprestador):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT *
                       FROM servicos
                       WHERE servicos.nome LIKE '%{}%' AND servicos.idprestador = {}
                """ .format(parteNome, idprestador)
                )

        listagem = list()
        for registro in cursor.fetchall():
            # (id, nome, descricao, preco, idprestador)
            servico = Servico(registro[0], registro[1], registro[2], registro[3], registro[4])
            listagem.append(servico)

        conn.close()
        return listagem

    def AtualizarServico(self, dadosServico):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()
        cursor.execute("""
               UPDATE servicos
               SET nome = ?, descricao = ?, preco = ?
               WHERE id = ? """,
               (dadosServico.nome, dadosServico.descricao, dadosServico.preco, dadosServico.id)
        )

        conn.commit()
        conn.close()


    def ExcluirServico(self, servico):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM servicos WHERE id = ?", (str(servico.id),))

        conn.commit()
        conn.close()

    def BuscaServicoPorId(self, id):
        conn = sqlite3.connect('ifavor.db')
        cursor = conn.cursor()
        # cursor.execute("SELECT * FROM servicos WHERE id = ?", (str(id),))
        cursor.execute("""
                       SELECT
                            servicos.id AS id,
                            servicos.nome AS nome,
                            servicos.descricao AS descricao,
                            servicos.preco AS preco,
                            prestadores.id AS idprestador,
                            prestadores.nome AS nome_prestador
                       FROM servicos
                       INNER JOIN prestadores ON servicos.idprestador = prestadores.id
                       WHERE servicos.id = {}
                """ .format(id)
                )

        registro = cursor.fetchone()
        conn.close()

        if registro != None:
            return Servico(registro[0], registro[1], registro[2], registro[3], registro[4], nome_prestador = registro[5])
        else:
            return None
