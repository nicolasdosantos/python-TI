class Calcular:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


    def calcular(self):
        pass


class Adicao(Calcular):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)


    def calcular(self):
        return self.num1 + self.num2


class Subtracao(Calcular):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def calcular(self):
        return self.num1 - self.num2


class Multiplicacao(Calcular):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def calcular(self):
        return self.num1 * self.num2


class Divisao(Calcular):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def calcular(self):
        return self.num1 / self.num2