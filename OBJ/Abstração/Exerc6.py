class Lampada:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print("Lâmpada ligada.")

    def desligar(self):
        self.ligada = False
        print("Lâmpada desligada.")

    def verificar_estado(self):
        if self.ligada:
            print("A lâmpada está ligada.")
        else:
            print("A lâmpada está desligada.")

minha_lampada = Lampada()

minha_lampada.verificar_estado()

minha_lampada.ligar()

minha_lampada.verificar_estado()

minha_lampada.desligar()

minha_lampada.verificar_estado()
