class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_valor(self):
        pass

class Produto(Item):
    def __init__(self,nome,preco, quantidade):
        super().__init__(nome,preco)
        self.quantidade = quantidade


    def calcular_valor(self):
        return self.quantidade * self.preco


class Servico(Item):
    def __init__(self,nome,preco, horas):
        super().__init__(nome,preco)
        self.horas = horas

    def calcular_valor(self):
        return self.horas * self.preco