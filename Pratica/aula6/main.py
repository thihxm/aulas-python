from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from random import randint
from AgendaIntegrada import BancodeDadosContatos, Contatos

class Linha(BoxLayout):
    nome = StringProperty('')
    telefone = StringProperty('')
    id = NumericProperty(0)
    
    def exibir_detalhes(self):
        App.get_running_app().id_atual = self.id

        App.get_running_app().sm.transition.direction = 'left'
        App.get_running_app().sm.current = 'detalhes'

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def popular_listagem(self, busca):
        self.ids.listagem.data = list()

        db = BancodeDadosContatos()
        contatos = db.ListarContatosPorNome(busca)

        for contato in contatos:
            self.ids.listagem.data.append({ 'id': contato.id, 'nome': contato.nome })
    
    def novo_contato(self):
        App.get_running_app().id_atual = 0

        self.manager.transition.direction = 'left'
        self.manager.current = 'detalhes'
    
class Visualizar(Screen):
    def preencher_detalhes(self):
        id = App.get_running_app().id_atual

        if id == 0:
            self.ids.txNome.text = ''
            self.ids.txTelefone.text = ''
            self.ids.txEmail.text = ''
            self.contato_atual = None
            self.bloquear_campos(False)
        else:
            db = BancodeDadosContatos()
            self.contato_atual = db.BuscaContatoPorId(id)
            self.ids.txNome.text = self.contato_atual.nome
            self.ids.txTelefone.text = self.contato_atual.telefone
            self.ids.txEmail.text = self.contato_atual.email
            self.bloquear_campos(True)

    def bloquear_campos(self, bloquear):
        self.ids.txNome.disabled = bloquear
        self.ids.txTelefone.disabled = bloquear
        self.ids.txEmail.disabled = bloquear
        if bloquear:
            self.ids.btnEditar.text = 'Editar'
            self.ids.btnExcluir.disabled = False
        else:
            self.ids.btnEditar.text = 'Salvar'
            self.ids.btnExcluir.disabled = True

    def voltar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'principal'

    def editar(self):
        if self.ids.btnEditar.text == 'Editar':
            self.bloquear_campos(False)
        else:
            db = BancodeDadosContatos()
            if not self.contato_atual:
                novo_contato = Contatos(None, self.ids.txNome.text, self.ids.txTelefone.text, self.ids.txEmail.text)
                db.CadastrarContato(novo_contato)
                self.voltar()
            else:
                self.contato_atual.nome = self.ids.txNome.text
                self.contato_atual.telefone = self.ids.txTelefone.text
                self.contato_atual.email = self.ids.txEmail.text
                db.AtualizarContato(self.contato_atual)
                self.bloquear_campos(True)

    def excluir(self):
        db = BancodeDadosContatos()
        db.ExcluirContato(self.contato_atual)
        self.voltar()

        
class AgendaContatosApp(App):
    def build(self):
        
        Window.size = (300, 400)
        self.id_atual = 0
        
        self.sm = ScreenManager()
        self.sm.add_widget(Principal(name='principal'))
        self.sm.add_widget(Visualizar(name='detalhes'))
        return self.sm
    
AgendaContatosApp().run()