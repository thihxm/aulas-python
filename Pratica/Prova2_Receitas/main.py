from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import sqlite3

class Ingrediente(object):
    def __init__(self, id, nome, quantidade, unidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
    
class BancodeDadosReceitas:    
    def CadastrarIngrediente(self, novoingrediente):
        conn = sqlite3.connect('receitas.db')
        cursor = conn.cursor()
        
        cursor.execute("""
                INSERT INTO ingrediente (id, nome, quantidade, unidade)
                VALUES (?, ?, ?, ?)
                """,
                (novoingrediente.id, novoingrediente.nome, novoingrediente.quantidade, novoingrediente.unidade)
                )
        
        conn.commit()
        conn.close()

    def ContarIngredientes(self):
        conn = sqlite3.connect('receitas.db')
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT COUNT(id) 
                       FROM ingrediente
                """)
        
        quantidade = cursor.fetchone()[0]

        conn.close()
        return quantidade

class Principal(BoxLayout):
    def cadastrar_ingrediente(self):
        db = BancodeDadosReceitas()
        novo_ingrediente = Ingrediente(None, self.ids.nome_ingrediente.text, self.ids.quantidade_ingrediente.text, self.ids.unidade_ingrediente.text)
        db.CadastrarIngrediente(novo_ingrediente)
        self.contar_ingredientes()

    def contar_ingredientes(self):
        db = BancodeDadosReceitas()
        resultado = db.ContarIngredientes()
        self.ids.mensagem_total.text = str(resultado)
        
class ProvaApp(App):
    def build(self):
        Window.size = (300,400)
        return Principal()
    
ProvaApp().run()
