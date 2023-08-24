class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto):
    def __init__(self,nome, preco):
        super(self).__init__(nome, preco,autor)
        self.autor = autor

class Eletronico(Produto):
    def __init__(self,nome, preco):
        super(self).__init__(nome, preco,voltagem)
        self.voltagem = voltagem