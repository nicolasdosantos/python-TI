teste = int(input("Quantas vezes voce ira testar o programa?"))

for i in range(teste):
    num1 = int(input("Digite seu primeiro numero inteiro"))
    num2 = int(input("Digite seu segundo numero inteiro"))
    if num1 %2 == 0:
        print(f"O MDC dos numero {num1} e {num2}, é {num2 % num1}")
    else:
        print(f"O MDC dos numero {num1} e {num2}, é {num1 % num2}")
