class Cliente():
  def __init__(self, nome, cpf, *args):
    self.nome = nome
    self.__cpf = cpf
    self.produtos = list(args)
  
  def get_cpf(self):
    return self.__cpf

class Produto():
  def __init__(self, id, descricao, preco, desconto):
    self.id = id
    self.descricao = descricao
    self.preco = preco
    self.desconto = desconto
  
  def preco_venda(self):
    return (self.preco - 0.01 * self.desconto * self.preco)
  
  def desconto_adic(self):
    preco_de_venda = self.preco_venda()
    if (preco_de_venda > 1000):
      return (preco_de_venda - 0.01 * 2 * preco_de_venda)
prod1 = Produto('produto 1', 'Meu produto 1', 10, 10)
prod2 = Produto('produto 2', 'Meu produto 2', 100, 10)
prod3 = Produto('produto 3', 'Meu produto 3', 1500, 10)
cliente = Cliente('Thiago', '123.456.789-01', prod1, prod2, prod3)

for produto in cliente.produtos:
  print('-'*40)
  print('Descrição: ', produto.descricao)
  print('Preço: ', produto.preco)
  print('Desconto: ', produto.desconto, '%')
  print('Preço Venda: ', produto.preco_venda())
  print('Desconto Adicional: ', produto.desconto_adic())
  print('-'*40)