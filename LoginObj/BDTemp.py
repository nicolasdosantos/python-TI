class Pessoa:
    def __init__(self, login, nome, cpf, genero, data, senha):
        self.login = login
        self.nome = nome
        self.cpf = cpf
        self.genero = genero
        self.data = data
        self.senha = senha


ListaPessoa = []


def CadastrarBD(login, nome, cpf, genero, data, senha):
    Obj = Pessoa(login, nome, cpf, genero, data, senha)
    ListaPessoa.append(Obj)


def AutenticarBD(login,senha):
    if not ListaPessoa:
        return "Vazia"
    else:
        for user in ListaPessoa:
            if user.login == login and user.senha == senha:
                return "Certo"


        return "Errado"