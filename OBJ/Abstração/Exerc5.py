class Aluno:
    def __init__(self,nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

Jorge = Aluno("Jorge", 10,7)
print("O aluno", Jorge.nome, "ficou com a media de: ", Jorge.calcular_media())