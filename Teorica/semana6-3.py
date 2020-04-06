# coding: utf-8


class Documento():
    def __init__(self, lista_autores, data):
        self.lista_autores = lista_autores
        self.data = data

    def get_lista_autores(self):
        return self.lista_autores

    def add_autor(self, autor):
        self.lista_autores.append(autor)


class Livro(Documento):
    def __init__(self, lista_autores, data, titulo, numero_copias):
        super().__init__(lista_autores, data)
        self.titulo = titulo
        self.numero_copias = numero_copias

    def get_numero_copias(self):
        return self.numero_copias

    def add_copia(self, numero):
        self.numero_copias += numero


class Email(Documento):
    def __init__(self, lista_autores, data, assunto, destinatarios, anexos):
        super().__init__(lista_autores, data)
        self.assunto = assunto
        self.destinatarios = destinatarios
        self.anexos = anexos

    def add_destinatarios(self, *args):
        for destinatario in args:
            self.destinatarios.append(destinatario)

    def get_lista_destinatarios(self):
        return self.destinatarios

    def get_lista_anexos(self):
        return self.anexos

    def add_anexos(self, *args):
        for anexo in args:
            self.anexos.append(anexo)


class Tese(Documento):
    def __init__(self, lista_autores, data, lista_abreviacoes, numero_capitulos, hipotese):
        super().__init__(lista_autores, data)
        self.lista_abreviacoes = lista_abreviacoes
        self.numero_capitulos = numero_capitulos
        self.hipotese = hipotese

    def get_hipotese(self):
        return self.hipotese

    def set_hipotese(self, hipotese):
        self.hipotese = hipotese

    def add_abreviacoes(self, *args):
        for abreviacao in args:
            self.lista_abreviacoes.append(abreviacao)

    def get_lista_abreviacoes(self):
        return self.lista_abreviacoes


livro1 = Livro([], '01/01/1970', 'Neuromancer', 3)
livro1.add_autor('Willian Gibson')
livro1.add_autor('João da Silva')
print(f'Título do livro: {livro1.titulo}')
print(f'Número de cópias: {livro1.get_numero_copias()}')
print(f'Autor(es) do livro: {livro1.get_lista_autores()}')
livro1.add_copia(2)
print(f'Novo número de cópias: {livro1.get_numero_copias()}')

email1 = Email([], '01/01/2020', 'Assuntos aleatórios', [], [])
email1.add_autor('Thiago')
email1.add_destinatarios('João', 'Maria', 'Pedro')
email1.add_anexos('imagem.png', 'arquivo.docx', 'planilha.xlsx')
print(f'Autor do email: {email1.get_lista_autores()}')
print(f'Destinatários do email: {email1.get_lista_destinatarios()}')
print(f'Data de envio: {email1.data}')
print(f'Assunto: {email1.assunto}')
print(f'Anexos: {email1.get_lista_anexos()}')

tese1 = Tese([], '01/01/2020', [], 10, 'Hipótese Teste')
tese1.add_autor('Thiago')
tese1.add_abreviacoes('TCP/IP', 'BR', 'P2P', 'IA')
print(f'Hipótese da tese: {tese1.get_hipotese()}')
print(f'Autores da teste: {tese1.get_lista_autores()}')
print(f'Número de capítulos: {tese1.numero_capitulos}')
print(f'Lista de abreviações: {tese1.get_lista_abreviacoes()}')
tese1.set_hipotese('Hipótese Top')
print(f'Nova hipótese da tese: {tese1.get_hipotese()}')
