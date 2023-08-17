primo = 0
normal = 0
while True:
    num = int(input("Digite um numero positivo: "))
    if num %2 == 0 and num %5 != 0:
        print("Seu numero não é primo")
    if num == 2:
        print("Seu numero é primo")