class Produto:
    def __init__(self,nome,preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def Vender (self, itens_vendidos):
        self.itens_vendidos = itens_vendidos
        return self.estoque - self.itens_vendidos

    def Mostrar (self):
        print("Estoque: ", self.itens_vendidos)


Goiaba = Produto("Basinga", 8, 25)
Goiaba.Vender(5)
Goiaba.Mostrar()