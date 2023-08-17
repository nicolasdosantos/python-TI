num = 0
num2 = 0
adicao = num + num2
sub = num - num2
multi = num * num2
while True:
    num = int(input("Digite seu primeiro numero"))
    num2 = int(input("Digite seu segundo numero"))
    cal = int(input("Qual operação voce ira esolher?\nAdição(1)\nSubtração(2)\nMultiplicação(3)\nDivisão(4)\nR:"))
    if cal == 1:
        print(f"Sua operação esscolhida foi adição e esse é o resultado {adicao}")
    elif cal == 2:
        print(f"Sua operação escolhida foi subtração e esse é o resultado {sub}")
    elif cal == 3:
        print(f"Sua operação escolhida foi multiplicação e esse é o resultado {multi}")
    elif cal == 4:
        print(f"Sua operação escolhida foi disão e esse é o resultado {num/num2}")