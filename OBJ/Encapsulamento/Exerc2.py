class Conta:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.titular = titular

    def depositar(self):
        q = int(input('Qual a quantidade sera depositada'))
        q += self.__saldo
        print("Deposito feito com sucesso")
        print("Seu saldo atual é de", self.__saldo)