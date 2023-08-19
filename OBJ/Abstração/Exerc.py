class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


Menino = Pessoa('Yago', 18)
Menina = Pessoa('Yasmin', 26)

print("O nome do menino é ", Menino.nome, "sua idade é", Menino.idade ,"E o nome da menina é ", Menina.nome, "E sua idade é", Menina.idade)