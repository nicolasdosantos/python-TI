class cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print("Woof!")


Raski = cachorro("Trovoada", 9)
print("O nome do cachoro é", Raski.nome, "sua idade é", Raski.idade)
Raski.latir()