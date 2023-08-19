class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


Menino = Pessoa('Yago', 18, "Homem")
Menina = Pessoa('Yasmin', 26, "Mulher")

print("O nome do menino é ", Menino.nome, "sua idade é", Menino.idade ,"E o nome da menina é ", Menina.nome, "E sua idade é", Menina.idade)