class Emprego:
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Emprego):
    def __init__(self,nome, salario):
        super().__init__(nome,salario,setor)
        self.setor = setor