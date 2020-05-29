from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from random import randint

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
    
        self.ids.listagem.data = [{'id': x, 'nome': str(x + 1), 'telefone': f'9{str(randint(10000000, 99999999))}'} for x in range(20)]
    
class Visualizar(Screen):
    def preencher_detalhes(self):
        id = App.get_running_app().id_atual
        
        self.ids.nome_contato.text = str(id)

    def voltar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'principal'

        
class AgendaContatosApp(App):
    def build(self):
        
        Window.size = (300, 400)
        self.id_atual = 0
        
        self.sm = ScreenManager()
        self.sm.add_widget(Principal(name='principal'))
        self.sm.add_widget(Visualizar(name='detalhes'))
        return self.sm
    
AgendaContatosApp().run()