def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero >= 0:
        return numero ** 0.5
    else:
        return "Número negativo não possui raiz real."

def media(*numeros):
    return sum(numeros) / len(numeros)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return 0.5 * base * altura


def hipotenusa(cateto_a, cateto_b):
    return (cateto_a ** 2 + cateto_b ** 2) ** 0.5


def area_quadrado(lado):
    return lado ** 2

def volume_cubo(aresta):
    return aresta ** 3

def juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo
    montante = capital + juros
    return juros, montante


def juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    juros = montante - capital
    return juros, montante