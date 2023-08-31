class Cliente:
    def __init__(self,nome,idade,codigo):
        self.nome = nome
        self.idade = idade
        self.__codigo = codigo


pessoa = Cliente("Bob", 22, 1856)
print(pessoa._Cliente__codigo)