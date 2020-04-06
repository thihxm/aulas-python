# coding: utf-8

class Endereco():
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.__CEP = cep

    def get_CEP(self):
        return self.__CEP


class Pessoa():
    def __init__(self, nome, endereco, idade, cpf, nickname):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__CPF = cpf
        self.nickname = nickname

    def get_nome(self):
        return self.__nome

    def get_CPF(self):
        return self.__CPF

    def get_endereco(self):
        return self.__endereco

    def set_nome(self, nome):
        self.__nome = nome


casa = Endereco('Rua Wagia Kassab Khury', 251,
                'Curitiba', 'Paraná', '82210-100')
eu = Pessoa('Thiago', casa, 19, '080.854.089-02', 'thihxm')

print(eu.get_nome())
print(eu.get_CPF())
print(eu.get_endereco().get_CEP())
eu.set_nome('Thiago Medeiros')
print(eu.get_nome())
