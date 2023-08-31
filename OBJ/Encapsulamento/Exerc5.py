class Restaurante:
    def __init__(self, nome, tipo, gasto_mensal):
        self.nome = nome
        self.tipo = tipo
        self.__gasto_mensal = gasto_mensal

    def mostar(self):
        print(self.nome)
        print(self.tipo)
        print(self.__gasto_mensal)

    def mudar(self):
        a = str(input("Qual sera o tipo novo do restaurante"))
        a == self.tipo