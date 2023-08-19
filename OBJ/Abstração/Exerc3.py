class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def saldo_da_conta(self,saldo):
        print("O saldo atual da conta é", saldo)

    def depositar(self):
        print("Quantia deposidata com sucesso!")

    def sacar(self):
        print("Sacando dinheiro")

Nicolas = ContaBancaria("Nicolas", 6000, 1)
Basinga = ContaBancaria("Basinga", 8000, 2)

Nicolas.saldo_da_conta(6000)