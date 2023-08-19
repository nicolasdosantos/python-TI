#class carro:
#    Marca = ''
#    Ano = 0
#    Nome = ''
#    def Ligar(self):
#        print('Ligando o', self.Nome)
#    Cor = ''
#    NumPortas = 2
#    VeloMax = 0

#CitroenC3 = carro()
#CitroenC3.Marca = 'Citroen'
#CitroenC3.Ano = 2020
#CitroenC3.Nome = "CitroenC3"
#CitroenC3.Cor = 'Branco'
#CitroenC3.NumPortas = 4
#CitroenC3.VeloMax = 173

#print('A cor do carro é', CitroenC3.Cor)
#CitroenC3.Ligar()

class carro:
    def __init__(self,nome,cor,ano):
        self.nome = nome
        self.cor = cor
        self.ano = ano


Fusca = carro('Fusca', 'Azul', 1965)
print('O nome do carro é', Fusca.nome)