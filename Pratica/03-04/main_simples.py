# coding: utf-8
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Quadro(BoxLayout):
    def __init__(self, **kwargs):
        super(Quadro, self).__init__(**kwargs)
        self.input_1 = self.ids.input_1
        self.input_2 = self.ids.input_2
        self.resultado = self.ids.resultado

    def somar(self):
        soma = float(self.input_1.text) + float(self.input_2.text)
        if(soma.is_integer()):
            soma = int(soma)
        self.resultado.text = str(soma)

    def subtrair(self):
        subtracao = float(self.input_1.text) - float(self.input_2.text)
        if(subtracao.is_integer()):
            subtracao = int(subtracao)
        self.resultado.text = str(subtracao)

    def multiplicar(self):
        multiplicacao = float(self.input_1.text) * float(self.input_2.text)
        if(multiplicacao.is_integer()):
            multiplicacao = int(multiplicacao)
        self.resultado.text = str(multiplicacao)

    def dividir(self):
        divisao = float(self.input_1.text) / float(self.input_2.text)
        if(divisao.is_integer()):
            divisao = int(divisao)
        self.resultado.text = str(divisao)


class Calculadora_SimplesApp(App):
    def build(self):
        return Quadro()


calculadora = Calculadora_SimplesApp()
calculadora.run()
