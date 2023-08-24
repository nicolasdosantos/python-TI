class Forma:
    def __init__(self,largura, altura):
        self.largura =largura
        self.altura =altura

    def area(self):
        return self.largura * self.altura

class Retangulo(Forma):
    def __init__(self,largura, altura):
        super().__init__(self,largura, altura)


class Triangulo(Forma):
    def __init__(self,largura, altura):
        super().__init__(self,largura, altura)

    def area(self):
        return self.largura * self.altura/2
