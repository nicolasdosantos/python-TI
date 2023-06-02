pares = 0
impar = 0

for i in range(7):
    num = int(input("Digite um numero"))
    if num %2 == 0:
        pares += 1
    if num %2 != 0:
        impar += 1
print(f"Voce digitou {pares} numero pares e {impar} numero impares")