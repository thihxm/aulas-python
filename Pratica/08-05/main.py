from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

class Jogadores(Screen):

  def jogar(self):
    App.get_running_app().som_inicio.play()

    self.manager.transition.direction = 'left'
    self.manager.current = 'jogo'

class Jogo(Screen):
  def vitoria(self):
    App.get_running_app().resultado = 'vitoria'
    self.manager.current = 'final'

  def empate(self):
    App.get_running_app().resultado = 'empate'
    self.manager.current = 'final'

class Final(Screen):
  def verificar_resultado(self):
    mensagem = self.ids.mensagem
    if App.get_running_app().resultado == 'vitoria':
      mensagem.text = 'Vitória'
      App.get_running_app().som_vitoria.play()
    else:
      mensagem.text = 'Empate'
      App.get_running_app().som_empate.play()

  def novo_jogo(self):
    self.manager.transition.direction = 'right'
    self.manager.current = 'jogadores'

  def sair(self):
    App.get_running_app().stop()

class JogoDaVelhaApp(App):
  def build(self):
      
    Window.size = (300,400)

    self.resultado = ''

    self.som_inicio = SoundLoader.load('here-we-go.wav')
    self.som_beep = SoundLoader.load('beep.wav')
    self.som_vitoria = SoundLoader.load('cheer.wav')
    self.som_empate = SoundLoader.load('tie.wav')

    sm = ScreenManager()
    sm.add_widget(Jogadores(name="jogadores"))
    sm.add_widget(Jogo(name="jogo"))
    sm.add_widget(Final(name="final"))
    
    return sm
    
JogoDaVelhaApp().run()
