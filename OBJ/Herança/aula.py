class Carro:
    def __init__(self, nome, cor, marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca

    def Ligar(self):
        print("Ligando o ", self.nome)


#class CarroCitroen(Carro):
 #   def __init__(self, nome, cor,portas):
#        super().__init__(nome, cor, "Citro")
#        self.portas = portas


class Carro2:
    def __init__(self,ano):
        self.ano = ano
    def Farol(self):
        print("Acendendo as luzes")

    def Acelerar(self):
        print("Acelerando...")



class CarroCitroen(Carro,Carro2):
    def __init__(self,nome,cor,portas,ano):
        Carro.__init__(self,nome,cor, "Citroen")
        Carro2.__init__(self,ano)
        self.portas = portas


Car = CarroCitroen("Cactus", "Azul", 2, 2022)
Car1 = CarroCitroen("C3", "Branco")
Car2 = CarroCitroen("Cactus", "Azul")
print("O nome do carro 1 é", Car1.nome)