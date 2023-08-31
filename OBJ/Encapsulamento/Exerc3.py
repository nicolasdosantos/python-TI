class Carro:
    def __init__(self,marca , modelo):
        self.__marca = marca
        self.__modelo = modelo

    def infor(self):
        print("A marca do carro é", self.__marca)
        print("A modelo do carro é", self.__modelo)

    def alterar(self):
        n = str(input("Qual sera o novo modelo"))
        n == self.__modelo
        print("Modelo alterado")