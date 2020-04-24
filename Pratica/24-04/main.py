from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Principal(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
class PlanetaApp(App):
    def build(self):
        self.title = 'Planetas'
        return Principal()
    
PlanetaApp().run()    
        
