class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_detalhes(self):
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Ano:",self.ano)


Fusca = Carro('Fusca', 'conversivel', 2020)
Fusca.mostrar_detalhes()