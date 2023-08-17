num1 = float(input("Insira um numero com casa decimal"))
num2 = float(input("Insira um numero para fazer a conta"))
conta = int(input("Qaul metodo vc quer usar?\nAdição(1),\nSubtração(2),\nMultiplicação(3),\nDivisão(4)"))
adicao = num1 + num2
sub = num1 - num2
multi = num1*num2
div = num1/num2
if conta == 1:
    print(f"Seu calculo de adição deu {adicao}")
elif conta == 2:
    print(f"Seu calculo de subtração deu {sub}")
elif conta == 3:
    print(f"Seu calculo de multiplicação deu {multi}")
elif conta == 4:
    print(f"Seu calculo de divisão deu {div}")