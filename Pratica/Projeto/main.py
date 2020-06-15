from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.properties import StringProperty, NumericProperty
from random import randint
from Ifavor import BancodeDadosServicos, Servico, BancodeDadosPedidos, Pedido, BancodeDadosUsuarios, Usuario

class MeuBotao(Button):
    tipo = StringProperty('info')
    def __init__(self, **kwargs): 
        super(MeuBotao, self).__init__(**kwargs)
        if self.tipo == 'edit':
            source = 'imagens/edit.png'
        elif self.tipo == 'cross':
            source = 'imagens/cross.png'
        elif self.tipo == 'check':
            source = 'imagens/check.png'
        else:
            source = 'imagens/info.png'
        self.size_hint = (None, None)
        self.height = 30
        self.width = self.height
        with self.canvas:
            self.rect = Rectangle(source = source) 
  
            self.bind(pos = self.update_rect, size = self.update_rect)
  
    def update_rect(self, *args): 
        self.rect.pos = (self.pos[0] + (self.width - 20) / 2, self.pos[1] + (self.height - 20) / 2)
        self.rect.size = (20, 20)

class Linha(BoxLayout):
    nome_servico = StringProperty('')
    nome = StringProperty('')
    id_servico = NumericProperty(0)
    id_pedido = NumericProperty(0)
    
    def exibir_detalhes(self):
        App.get_running_app().id_servico_atual = self.id_servico
        App.get_running_app().id_pedido_atual = self.id_pedido

        App.get_running_app().sm.transition.direction = 'left'
        App.get_running_app().sm.current = 'detalhesCliente'

class LinhaPrestador(BoxLayout):
    nome_servico = StringProperty('')
    nome = StringProperty('')
    tipo_botoes = StringProperty('')
    id_servico = NumericProperty(0)
    id_pedido = NumericProperty(0)

    def __init__(self, **kwargs):
        super(LinhaPrestador, self).__init__(**kwargs)
    
    def on_tipo_botoes(self, *args):
        for widget in self.walk(restrict = True):
            if type(widget) == MeuBotao:
                self.ids.container.remove_widget(widget)
        if self.tipo_botoes == 'editar':
            btnEditar = MeuBotao(tipo = 'edit')
            # btnEditar.bind(on_release = self.exibir_detalhes)
            self.ids.container.add_widget(btnEditar)
        elif self.tipo_botoes == 'acoes':
            btnAceitar = MeuBotao(tipo = 'check')
            btnAceitar.bind(on_release = self.aceitar_pedido)
            btnRecusar = MeuBotao(tipo = 'cross')
            btnRecusar.bind(on_release = self.rejeitar_pedido)
            self.ids.container.add_widget(btnRecusar)
            self.ids.container.add_widget(btnAceitar)
        else:
            btnInfo = MeuBotao(tipo = 'info')
            btnInfo.bind(on_release = self.exibir_detalhes_cliente)
            self.ids.container.add_widget(btnInfo)

    def exibir_detalhes_cliente(self, *args):
        App.get_running_app().id_servico_atual = self.id_servico
        App.get_running_app().id_pedido_atual = self.id_pedido

        App.get_running_app().sm.transition.direction = 'left'
        App.get_running_app().sm.current = 'prestadorInfoCliente'

    def aceitar_pedido(self, *args):
        db_pedidos = BancodeDadosPedidos()
        db_pedidos.AceitarPedido(self.id_pedido)
        App.get_running_app().sm.get_screen('principalPrestador').popular_listagem('')

    def rejeitar_pedido(self, *args):
        db_pedidos = BancodeDadosPedidos()
        db_pedidos.ExcluirPedido(self.id_pedido)
        App.get_running_app().sm.get_screen('principalPrestador').popular_listagem('')

class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def entrar(self):
        usuario = self.ids.txUsuario.text
        senha = self.ids.txSenha.text
        if usuario != '' and senha != '':
            db_usuarios = BancodeDadosUsuarios()
            self.usuario_atual = db_usuarios.BuscaUsuarioCredenciais(usuario, senha)
            if self.usuario_atual:
                self.manager.transition.direction = 'left'
                if self.usuario_atual.tipo == 0:
                    App.get_running_app().id_cliente = self.usuario_atual.id
                    self.manager.current = 'principalCliente'
                else:
                    App.get_running_app().id_prestador = self.usuario_atual.id
                    self.manager.current = 'principalPrestador'

    def habilitar_botao(self):
        if self.ids.txSenha.text == '' or self.ids.txUsuario.text == '':
            self.ids.btnEntrar.disabled = True
        else:
            self.ids.btnEntrar.disabled = False

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
        self.manager.transition.direction = 'left'
        self.manager.current = 'detalhesCliente'

    def sair(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'
        App.get_running_app().id_servico_atual = 0
        App.get_running_app().id_pedido_atual = 0
        App.get_running_app().id_cliente = 0
        App.get_running_app().id_prestador = 0

class VisualizarCliente(Screen):
    def preencher_detalhes(self):
        self.id_servico = App.get_running_app().id_servico_atual
        self.id_pedido = App.get_running_app().id_pedido_atual
        self.id_cliente = App.get_running_app().id_cliente

        if self.id_servico != 0:
            db_servicos = BancodeDadosServicos()
            self.servico_atual = db_servicos.BuscaServicoPorId(self.id_servico)
            self.ids.txNomeServico.text = self.servico_atual.nome
            self.ids.txNomePrestador.text = self.servico_atual.nome_prestador
            self.ids.txDescricaoServico.text = self.servico_atual.descricao
            self.ids.txPreco.text = f'R$ {self.servico_atual.preco}'
            self.pedido_atual = None
            self.alterar_botao_pedido(False)
        elif self.id_pedido != 0:
            db_pedidos = BancodeDadosPedidos()
            self.pedido_atual = db_pedidos.BuscaPedidoPorId(self.id_pedido)
            self.ids.txNomeServico.text = self.pedido_atual.nome_servico
            self.ids.txNomePrestador.text = self.pedido_atual.nome_prestador
            self.ids.txDescricaoServico.text = self.pedido_atual.descricao_servico
            self.ids.txPreco.text = f'R$ {self.pedido_atual.preco_servico}'
            self.servico_atual = None
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
                db_pedidos.ExcluirPedido(self.pedido_atual.id)
                self.voltar()
        else:
            if self.servico_atual:
                novo_pedido = Pedido(None, self.id_cliente, self.id_servico, False)
                db_pedidos.SolicitarPedido(novo_pedido)
                self.voltar()

class PrincipalPrestador(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def popular_listagem(self, busca):
        self.ids.listagemMeusServicos.data = list()
        self.ids.listagemServicos.data = list()

        db_servicos = BancodeDadosServicos()
        db_pedidos = BancodeDadosPedidos()
        servicos = db_servicos.ListarServicosPorNomeEPrestador(busca, App.get_running_app().id_prestador)
        meus_pedidos = db_pedidos.ListarPedidosPorNomeEPrestador(busca, App.get_running_app().id_prestador)

        for servico in servicos:
            self.ids.listagemMeusServicos.data.append({
                'id_servico': servico.id,
                'nome_servico': servico.nome,
                'nome': servico.nome_prestador,
                'tipo_botoes': 'editar'
            })
        for pedido in meus_pedidos:
            dados = {
                'id_pedido': pedido.id,
                'pedido_id_servico': pedido.idservico,
                'nome_servico': pedido.nome_servico,
                'nome': pedido.nome_cliente,
                'pedido_id_cliente': pedido.idcliente,
                'tipo_botoes': 'info'
            }
            if pedido.aceito == True:
                self.ids.listagemServicos.data.append(dados)
            else:
                dados['tipo_botoes'] = 'acoes'
                self.ids.listagemServicos.data.append(dados)
    
    def novo_contato(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'detalhesPrestador'

    def sair(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'
        App.get_running_app().id_servico_atual = 0
        App.get_running_app().id_pedido_atual = 0
        App.get_running_app().id_cliente = 0
        App.get_running_app().id_prestador = 0

class VisualizarPrestador(Screen):
    def preencher_detalhes(self):
        self.id_servico = App.get_running_app().id_servico_atual
        self.id_pedido = App.get_running_app().id_pedido_atual
        self.id_prestador = App.get_running_app().id_prestador

        if self.id_servico != 0:
            db_servicos = BancodeDadosServicos()
            self.servico_atual = db_servicos.BuscaServicoPorId(self.id_servico)
            self.ids.txNomeServico.text = self.servico_atual.nome
            self.ids.txNomePrestador.text = self.servico_atual.nome_prestador
            self.ids.txDescricaoServico.text = self.servico_atual.descricao
            self.ids.txPreco.text = f'R$ {self.servico_atual.preco}'
            self.pedido_atual = None
            self.alterar_botao_pedido(False)
        elif self.id_pedido != 0:
            db_pedidos = BancodeDadosPedidos()
            self.pedido_atual = db_pedidos.BuscaPedidoPorId(self.id_pedido)
            self.ids.txNomeServico.text = self.pedido_atual.nome_servico
            self.ids.txNomePrestador.text = self.pedido_atual.nome_prestador
            self.ids.txDescricaoServico.text = self.pedido_atual.descricao_servico
            self.ids.txPreco.text = f'R$ {self.pedido_atual.preco_servico}'
            self.servico_atual = None
            self.bloquear_campos(True)
        else:
            self.ids.txNomeServico.text = ''
            self.ids.txNomePrestador.text = ''
            self.ids.txDescricaoServico.text = ''
            self.ids.txPreco.text = ''
            self.servico_atual = None
            self.pedido_atual = None
            self.bloquear_campos(False)

    def bloquear_campos(self, bloquear):
        self.ids.txNomeServico.disabled = bloquear
        self.ids.txDescricaoServico.disabled = bloquear
        self.ids.txPreco.disabled = bloquear
        if bloquear:
            self.ids.btnAcao.text = 'Editar'
        else:
            self.ids.btnAcao.text = 'Salvar'

    def voltar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'principalPrestador'

    def editar(self):
        db_pedidos = BancodeDadosPedidos()
        if self.ids.btnAcao.text == 'Cancelar':
            if self.pedido_atual:
                db_pedidos.ExcluirPedido(self.pedido_atual.id)
                self.voltar()
        else:
            if self.servico_atual:
                novo_pedido = Pedido(None, self.id_cliente, self.id_servico, False)
                db_pedidos.SolicitarPedido(novo_pedido)
                self.voltar()

class PrestadorInfoCliente(Screen):
    def preencher_detalhes(self):
        self.id_pedido = App.get_running_app().id_pedido_atual

        if self.id_pedido != 0:
            db_pedido = BancodeDadosPedidos()
            db_usuarios = BancodeDadosUsuarios()
            self.pedido_atual = db_pedido.BuscaPedidoPorId(self.id_pedido)
            self.cliente_atual = db_usuarios.BuscaUsuarioPorId(self.pedido_atual.idcliente)
            self.ids.txNomeServico.text = self.pedido_atual.nome_servico
            self.ids.txNomeCliente.text = self.cliente_atual.nome
            self.ids.txEnderecoCliente.text = self.cliente_atual.endereco
            self.ids.txTelefoneCliente.text = self.cliente_atual.telefone
        else:
            self.ids.txNomeServico.text = ''
            self.ids.txNomeCliente.text = ''
            self.ids.txEnderecoCliente.text = ''
            self.ids.txTelefoneCliente.text = ''
            self.pedido_atual = None
            self.cliente_atual = None

    def voltar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'principalPrestador'

    def cancelar(self):
        db_pedidos = BancodeDadosPedidos()
        if self.pedido_atual:
            db_pedidos.ExcluirPedido(self.pedido_atual.id)
            self.voltar()

class IfavorApp(App):
    def build(self):
        
        Window.size = (300, 400)
        self.id_cliente = 0
        self.id_prestador = 0
        self.id_cliente_info = 0
        self.id_servico_atual = 0
        self.id_pedido_atual = 0
        
        self.sm = ScreenManager()
        self.sm.add_widget(Login(name='login'))
        self.sm.add_widget(PrincipalCliente(name='principalCliente'))
        self.sm.add_widget(VisualizarCliente(name='detalhesCliente'))
        self.sm.add_widget(PrincipalPrestador(name='principalPrestador'))
        self.sm.add_widget(VisualizarPrestador(name='detalhesPrestador'))
        self.sm.add_widget(PrestadorInfoCliente(name='prestadorInfoCliente'))
        return self.sm

IfavorApp().run()