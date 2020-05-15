from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.properties import StringProperty

class Principal(BoxLayout):
  planetas = {
    'Terra': {
      'image': 'terra.jpg',
      'color': '#ffffff'
    },
    'Lua': {
      'image': 'moon.jpg',
      'color': '#0000ff'
    },
    'Saturno': {
      'image': 'saturno.jpg',
      'color': '#ff00ff'
    },
    'Júpiter': {
      'image': 'jupiter.jpg',
      'color': '#00ffff'
    }
  }
  imagem_planeta = StringProperty('terra.jpg')

  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    Window.size = (300, 400)
    self.label_planeta = self.ids.label_planeta
    self.spinner_planetas = self.ids.spinner_planetas
    self.label_status_som = self.ids.label_status_som
    self.label_planeta.text = self.spinner_planetas.text

  def muda_planeta(self, planeta):
    planeta_atual = self.planetas[planeta]
    self.label_planeta.text = f'[color={planeta_atual["color"]}]{planeta}[/color]'
    self.imagem_planeta = planeta_atual['image']

  def habilitar_som(self, ativo):
    if ativo:
      self.label_status_som.text = 'Desativar som'
    else:
      self.label_status_som.text = 'Ativar som'

  def botao_sair(self):
    App.get_running_app().stop()

class PlanetaApp(App):
  def build(self):
    self.title = 'Planetas'
    return Principal()
    
PlanetaApp().run()    
        
