class Produto:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

Morango = Produto("Morango", 8, 25)
print("O produto ", Morango.nome, " tem um total de ", Morango.quantidade, " dentro do armazem, o valor total dessa quantia é de ", Morango.calcular_total())

