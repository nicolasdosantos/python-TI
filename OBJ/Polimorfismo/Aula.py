#class Profissao:
#    def açao(self):
#        pass


#class Estudante(Profissao):
#    def açao(self):
#        print("Estudante")


class Profissao:
    def açao(self):
        return 'A principal atividade é'


class Estudante(Profissao):
    def açao(self):
        print(super().açao(),"Estudar")