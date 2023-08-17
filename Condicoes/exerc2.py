num1 = int(input("Coloquei seu primeiro numero"))
num2 = int(input("Coloquei seu segundo numero"))
if num1 < num2:
    print(f"O {num2} é maior que {num1}")
elif num1 > num2:
    print(f"O {num1} é maior que {num2}")
elif num2 == num1:
    print(f"Os dois numeros são {num1}")
