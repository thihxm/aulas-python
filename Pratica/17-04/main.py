# coding: utf-8
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


class Quadro(BoxLayout):
    def __init__(self, **kwargs):
        super(Quadro, self).__init__(**kwargs)
        self.input_1 = self.ids.input_1
        self.input_2 = self.ids.input_2
        self.resultado = self.ids.resultado
        self.tipo_operacao = self.ids.tipo_operacao
        self.btn_calcular = self.ids.btn_calcular

    def calcular(self):
        operacao = self.tipo_operacao.text
        resultado = 0
        if operacao == 'soma':
            resultado = float(self.input_1.text) + float(self.input_2.text)
        elif operacao == 'subtracao':
            resultado = float(self.input_1.text) - float(self.input_2.text)
        elif operacao == 'multiplicacao':
            resultado = float(self.input_1.text) * float(self.input_2.text)
        elif operacao == 'divisao':
            resultado = float(self.input_1.text) / float(self.input_2.text)

        if resultado.is_integer():
            resultado = int(resultado)
        self.resultado.text = str(resultado)
    
    def mudar_frase(self, operacao):
        if operacao == 'soma':
            self.btn_calcular.text = 'Clique aqui para SOMAR'
        elif operacao == 'subtracao':
            self.btn_calcular.text = 'Clique aqui para SUBTRAIR'
        elif operacao == 'multiplicacao':
            self.btn_calcular.text = 'Clique aqui para MULTIPLICAR'
        elif operacao == 'divisao':
            self.btn_calcular.text = 'Clique aqui para DIVIDIR'

class CalculadoraApp(App):
    def build(self):
        return Quadro()


calculadora = CalculadoraApp()
calculadora.run()
