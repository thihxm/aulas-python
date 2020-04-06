# coding: utf-8


class Voo():
    def __init__(self, numero, origem, destino):
        self.__numero = numero
        self.origem = origem
        self.destino = destino

    def get_origem(self):
        return self.origem

    def get_destino(self):
        return self.destino


class CompanhiaAerea():
    def __init__(self, cnpj, nome, numero_aeronaves, *args)
    self.__CNPJ = cnpj
    self.nome = nome
    self.numero_aeronaves = numero_aeronaves
    self.list_voos = list(args)
