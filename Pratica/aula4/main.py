from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from random import randint

class Jogadores(Screen):
  def preencher_jogadores(self):
    self.ids.jogador1.text = App.get_running_app().nome_jogador1
    self.ids.jogador2.text = App.get_running_app().nome_jogador2

  def jogar(self):
    App.get_running_app().nome_jogador1 = self.ids.jogador1.text
    App.get_running_app().nome_jogador2 = self.ids.jogador2.text

    App.get_running_app().som_inicio.play()

    self.manager.transition.direction = 'left'
    self.manager.current = 'jogo'

class Jogo(Screen):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    self.botoes = (
      (self.ids.btn00, self.ids.btn01, self.ids.btn02),
      (self.ids.btn10, self.ids.btn11, self.ids.btn12),
      (self.ids.btn20, self.ids.btn21, self.ids.btn22),
    )
    self.simbolo_atual = 'X'
    self.jogador_atual = ''
    self.total_jogadas = 0

  def preparar_jogo(self):
    for linha in self.botoes:
      for botao in linha:
        botao.text = ''

    App.get_running_app().resultado = ''
    App.get_running_app().ganhador = ''
    self.total_jogadas = 0

    jogador_sorteado = randint(1, 2)
    if jogador_sorteado == 1:
      self.jogador_atual = App.get_running_app().nome_jogador1
    else:
      self.jogador_atual = App.get_running_app().nome_jogador2

    self.ids.label_jogador_atual.text = self.jogador_atual
  
  def verificar_linha(self):
    if self.botoes[0][0].text == self.botoes[0][1].text == self.botoes[0][2].text != '':
      if self.botoes[0][0].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2
    if self.botoes[1][0].text == self.botoes[1][1].text == self.botoes[1][2].text != '':
      if self.botoes[1][0].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2
    if self.botoes[2][0].text == self.botoes[2][1].text == self.botoes[2][2].text != '':
      if self.botoes[2][0].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2
  
  def verificar_coluna(self):
    if self.botoes[0][0].text == self.botoes[1][0].text == self.botoes[2][0].text != '':
      if self.botoes[0][0].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2
    if self.botoes[0][1].text == self.botoes[1][1].text == self.botoes[2][1].text != '':
      if self.botoes[0][1].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2
    if self.botoes[0][2].text == self.botoes[1][2].text == self.botoes[2][2].text != '':
      if self.botoes[0][2].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2
  
  def verificar_diagonal(self):
    if self.botoes[0][0].text == self.botoes[1][1].text == self.botoes[2][2].text != '':
      if self.botoes[0][0].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2
    if self.botoes[0][2].text == self.botoes[1][1].text == self.botoes[2][0].text != '':
      if self.botoes[0][2].text == 'X':
        App.get_running_app().ganhador = App.get_running_app().nome_jogador1
      else:
        App.get_running_app().ganhador = App.get_running_app().nome_jogador2

  def verificar_ganhador(self):
    self.verificar_linha()
    self.verificar_coluna()
    self.verificar_diagonal()
    if App.get_running_app().ganhador != '':
      self.vitoria()

  def jogar_posicao(self, linha, coluna):
    botao_clicado = self.botoes[linha][coluna]

    if botao_clicado.text != '':      
      return

    botao_clicado.text = self.simbolo_atual
    self.total_jogadas += 1

    self.verificar_ganhador()

    if self.total_jogadas == 9:
      self.empate()

    if self.simbolo_atual == 'X':
      self.simbolo_atual = 'O'
      self.jogador_atual = App.get_running_app().nome_jogador2
    else:
      self.simbolo_atual = 'X'
      self.jogador_atual = App.get_running_app().nome_jogador1
    self.ids.label_jogador_atual.text = self.jogador_atual

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
      mensagem.text = 'Vitória do(a) ' + App.get_running_app().ganhador
      App.get_running_app().som_vitoria.play()
    else:
      mensagem.text = 'Empate'
      App.get_running_app().som_empate.play()
      App.get_running_app().som_empate.seek(9)

  def novo_jogo(self):
    self.manager.transition.direction = 'right'
    self.manager.current = 'jogadores'

  def sair(self):
    App.get_running_app().stop()

class JogoDaVelhaApp(App):

  def build(self):
      
    Window.size = (300,400)

    self.resultado = ''
    self.ganhador = ''
    self.nome_jogador1 = 'joao'
    self.nome_jogador2 = 'maria'

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
