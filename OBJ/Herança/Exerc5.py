class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano =ano

class Moto(Veiculo):
    def __init__(self,marca,modelo,ano):
        super(self).__init__(marca,modelo,ano,cilindrada)
        self.cilindrada = cilindrada


class Carro(Veiculo):
    def __init__(self,marca,modelo,ano):
        super(self).__init__(marca,modelo,ano,portas,porta_mala)
        self.portas = portas
        self.porta_mala = porta_mala