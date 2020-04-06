from kivy.app import App
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        label = Label(text='Teste')
        return label


novo_app = MeuApp()
novo_app.run()
