from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import sqlite3

class Produto(object):
    def __init__(self, id, nome, quantidade, unidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
    
class BancodeDadosProdutos:    
    def IncluirNovoProduto(self, novo_produto):
        conn = sqlite3.connect('materiais.db')
        cursor = conn.cursor()
        
        cursor.execute("""
                INSERT INTO produto (id, nome, quantidade, unidade)
                VALUES (?, ?, ?, ?)
            """,
            (novo_produto.id, novo_produto.nome, novo_produto.quantidade, novo_produto.unidade)
        )
        
        conn.commit()
        conn.close()

    def ContarQuantidadeProdutos(self):
        conn = sqlite3.connect('materiais.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(id) 
            FROM produto
        """)
        
        total_produtos = cursor.fetchone()[0]

        conn.close()
        return total_produtos

class Principal(BoxLayout):
    def inserir_produto(self):
        db = BancodeDadosProdutos()
        novo_produto = Produto(None, self.ids.nome_produto.text, self.ids.quantidade_produto.text, self.ids.unidade_produto.text)
        db.IncluirNovoProduto(novo_produto)
        self.contar_quantidade_produtos()

    def contar_quantidade_produtos(self):
        db = BancodeDadosProdutos()
        total_produtos = db.ContarQuantidadeProdutos()
        self.ids.mensagem_total.text = str(total_produtos)
        
class ProvaApp(App):
    def build(self):
        Window.size = (300,400)
        return Principal()
    
ProvaApp().run()
