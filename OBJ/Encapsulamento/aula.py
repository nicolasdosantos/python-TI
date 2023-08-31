#class Anime:
#    def __init__(self, nome,categoria, idade):
#        self._nome = nome
#        self.categoria = categoria
#        self._idade = idade


#    def _assistir(self):
#        print('Assistindo o', self._nome)


#Anime1 = Anime("Baki", "Luta", 18)
#print('O nome do anime é', Anime1._nome)
#Anime1._assistir()



class Anime:
    def __init__(self, nome,categoria, idade):
        self.__nome = nome
        self.categoria = categoria
        self.__idade = idade


    def __assistir(self):
        print('Assistindo o', self.__nome)


Anime1 = Anime("Baki", "Luta", 18)
print('O nome do anime é', Anime1.__nome)
Anime1.__assistir()