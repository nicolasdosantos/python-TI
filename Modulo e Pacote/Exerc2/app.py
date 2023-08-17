import geometria

op = str(input("Qual operação voce ira fazer?\nArea de um quadrado(Q)\nArea de um circulo(C)\n")).lower()

if op == "q":
    lado = int(input("Digite um numero para o calculo:\n"))
    print(geometria.area_quadrado(lado))
elif op == "c":
    raio = int(input("Digite o valor do raio:\n"))
    print(geometria.area_circulo(raio))