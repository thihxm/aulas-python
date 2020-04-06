# coding: utf-8
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Quadro(BoxLayout):
    def __init__(self, **kwargs):
        super(Quadro, self).__init__(**kwargs)
        self.display = self.ids.display
        self.valores = []
        self.operacoes = []
        self.resultado = 0

    def add(self, number_as_string):
        if (number_as_string == '.'):
            if(len(self.display.text) > 0):
                if (not number_as_string in self.display.text):
                    self.display.text += number_as_string
            else:
                self.display.text = '0.'
        elif (number_as_string == '-'):
            if(len(self.display.text) > 0):
                first_negative = self.display.text[0]
                if (first_negative == number_as_string):
                    self.display.text = self.display.text[1:]
                else:
                    self.display.text = number_as_string + self.display.text
            else:
                self.display.text = number_as_string
        else:
            self.display.text += number_as_string

    def deletar(self):
        if (len(self.display.text) >= 1):
            self.display.text = self.display.text[:-1]

    def limpar_tudo(self):
        self.resultado = 0
        self.valores = []
        self.operacoes = []
        self.display.text = ''

    def somar(self):
        self.valores.append(float(self.display.text))
        self.operacoes.append('+')
        self.display.text = ''

    def subtrair(self):
        self.valores.append(float(self.display.text))
        self.operacoes.append('-')
        self.display.text = ''

    def multiplicar(self):
        self.valores.append(float(self.display.text))
        self.operacoes.append('*')
        self.display.text = ''

    def dividir(self):
        self.valores.append(float(self.display.text))
        self.operacoes.append('/')
        self.display.text = ''

    def igual(self):
        self.valores.append(float(self.display.text))
        self.display.text = ''
        for i in range(len(self.valores)):
            if(i == 0):
                self.resultado = self.valores[i]
            else:
                resultado_anterior = self.resultado
                if (0 < i <= len(self.operacoes)):
                    if (self.operacoes[i - 1] == '+'):
                        self.resultado += self.valores[i]
                    elif (self.operacoes[i - 1] == '-'):
                        self.resultado -= self.valores[i]
                    elif (self.operacoes[i - 1] == '*'):
                        self.resultado *= self.valores[i]
                    elif (self.operacoes[i - 1] == '/'):
                        self.resultado /= self.valores[i]
        if(self.resultado.is_integer()):
            self.resultado = int(self.resultado)
        self.display.text = str(self.resultado)
        self.valores = []
        self.operacoes = []


class CalculadoraApp(App):
    def build(self):
        return Quadro()


calculadora = CalculadoraApp()
calculadora.run()
