class Bebida:
    def __init__(self,nome , tipo):
        self.nome = nome
        self.tipo = tipo


class Refrigerante(Bebida):
    def __init__(self,nome, tipo):
        super().__init__(nome, tipo,latinha)
        self.latinha = latinha


class Cafe(Bebida):
    def __init__(self,nome,tipo):
        super().__init__(nome,tipo, acucar)
        self.acucar = acucar