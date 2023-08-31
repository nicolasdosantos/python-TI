class Livro:
    def __init__(self, titulo,autor, ano, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.preco = preco

    def atualizar(self,ano):
        a = str(input("Qual o ano atual"))
        a == self.ano

    def Mostrar(self):
        print(self.titulo)
        print(self.autor)
        print(self.ano)
        print(self.preco)

