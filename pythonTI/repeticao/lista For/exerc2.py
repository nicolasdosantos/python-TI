primo = 0
normal = 0
for i in range(5):
    num = int(input("Digite um numero positivo: "))
    if num %2 == 0 and num %5 != 0:
        normal += 1
    elif num == 2:
        primo += 1
    else:
        primo += 1
print(f"Voce digitou {normal} numeros normais, e {primo} numeros  primos")