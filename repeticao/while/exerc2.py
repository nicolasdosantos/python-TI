soma = 0
while True:
    num = int(input("Digete seu numero"))
    if num == 0:
        print("Voce saio do programa, inici-o denevo ")
    elif num % 2 == 0:
        soma += num
        print(f"Soma dos pares é de {soma}")
