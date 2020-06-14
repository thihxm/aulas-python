from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from random import randint
from Ifavor import BancodeDadosServicos, Servico, BancodeDadosPedidos, Pedido

class Linha(BoxLayout):
    nome_servico = StringProperty('')
    nome = StringProperty('')
    id_servico = NumericProperty(0)
    id_pedido = NumericProperty(0)
    
    def exibir_detalhes(self):
        App.get_running_app().id_atual = self.id_servico
        App.get_running_app().id_servico_atual = self.id_servico
        App.get_running_app().id_pedido_atual = self.id_pedido

        App.get_running_app().sm.transition.direction = 'left'
        App.get_running_app().sm.current = 'detalhes'

class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def entrar(self):
        if not self.ids.txSenha.text == '':
            if self.ids.txUsuario.text == 'cliente':
                self.manager.transition.direction = 'left'
                self.manager.current = 'principalCliente'

class PrincipalCliente(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def popular_listagem(self, busca):
        self.ids.listagemServicos.data = list()
        self.ids.listagemSolicitacoes.data = list()

        db_servicos = BancodeDadosServicos()
        db_pedidos = BancodeDadosPedidos()
        servicos = db_servicos.ListarServicosPorNome(busca)
        meus_pedidos = db_pedidos.ListarPedidosPorNomeECliente(busca, App.get_running_app().id_cliente)

        for servico in servicos:
            self.ids.listagemServicos.data.append({ 'id_servico': servico.id, 'nome_servico': servico.nome, 'nome': servico.nome_prestador })
        for pedido in meus_pedidos:
            self.ids.listagemSolicitacoes.data.append({ 'id_pedido': pedido.id, 'nome_servico': pedido.nome_servico, 'nome': pedido.nome_prestador })
    
    def novo_contato(self):
        App.get_running_app().id_atual = 0

        self.manager.transition.direction = 'left'
        self.manager.current = 'detalhes'

    def sair(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'
        App.get_running_app().id_servico_atual = 0
        App.get_running_app().id_pedido_atual = 0
        App.get_running_app().id_cliente = 0

class Visualizar(Screen):
    def preencher_detalhes(self):
        self.id_servico = App.get_running_app().id_servico_atual
        self.id_pedido = App.get_running_app().id_pedido_atual
        self.id_cliente = App.get_running_app().id_cliente

        if not self.id_servico == 0:
            db_servicos = BancodeDadosServicos()
            self.servico_atual = db_servicos.BuscaServicoPorId(self.id_servico)
            self.ids.txNomeServico.text = self.servico_atual.nome
            self.ids.txNomePrestador.text = self.servico_atual.nome_prestador
            self.ids.txDescricaoServico.text = self.servico_atual.descricao
            self.ids.txPreco.text = f'R$ {self.servico_atual.preco}'
            self.alterar_botao_pedido(False)
        elif not self.id_pedido == 0:
            db_pedidos = BancodeDadosPedidos()
            self.pedido_atual = db_pedidos.BuscaPedidoPorId(self.id_pedido)
            self.ids.txNomeServico.text = self.pedido_atual.nome_servico
            self.ids.txNomePrestador.text = self.pedido_atual.nome_prestador
            self.ids.txDescricaoServico.text = self.pedido_atual.descricao_servico
            self.ids.txPreco.text = f'R$ {self.pedido_atual.preco_servico}'
            self.alterar_botao_pedido(True)

    def alterar_botao_pedido(self, pedido):
        if pedido:
            self.ids.btnAcao.text = 'Cancelar'
        else:
            self.ids.btnAcao.text = 'Solicitar'

    def voltar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'principalCliente'

    def editar(self):
        db_pedidos = BancodeDadosPedidos()
        if self.ids.btnAcao.text == 'Cancelar':
            if self.pedido_atual:
                db_pedidos.ExcluirPedido(self.pedido_atual)
                self.voltar()
        else:
            if self.servico_atual:
                novo_pedido = Pedido(None, self.id_cliente, self.id_servico, False)
                db_pedidos.SolicitarPedido(novo_pedido)
                self.voltar()

class IfavorApp(App):
    def build(self):
        
        Window.size = (300, 400)
        self.id_atual = 0
        self.id_cliente = 1
        self.id_servico_atual = 0
        self.id_pedido_atual = 0
        
        self.sm = ScreenManager()
        self.sm.add_widget(Login(name='login'))
        self.sm.add_widget(PrincipalCliente(name='principalCliente'))
        self.sm.add_widget(Visualizar(name='detalhes'))
        return self.sm

IfavorApp().run()