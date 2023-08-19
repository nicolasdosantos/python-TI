class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular(self):
        return self.base * self.altura

Medida = Retangulo(10,10)
print(Medida.calcular())