class Pessoa:
  def __init__(self, id):
    self.id = id
class Professor(Pessoa):
  def __init__(self, id):
    super().__init__(id)
    self.id += 'P'
class Estudante(Pessoa):
  def __init__(self, id):
    super().__init__(id)
    self.id += 'E'
class AuxiliarEnsino(Estudante, Professor):
  def __init__(self, id):
    super().__init__(id)

x = AuxiliarEnsino('2675')
print(x.id)
y = Estudante('4567')
print(y.id)
z = Professor('3421')
print(z.id)
p = Pessoa('5749')
print(p.id)