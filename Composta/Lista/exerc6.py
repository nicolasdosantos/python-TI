num = []

p = int(input("Quantas vezes voce ira testas o programa?\n"))

for i in range(p):
    num.append(int(input("Digite um numero inteiro\n")))

print(f"A quantidade de numeros inserida na lista for de {len(num)}")
num.sort(reverse=True)
print(f"A lista em ordem decresente é assim: {num}")

if 5 in num:
    print(f"O numero 5 contem na lista")
else:
    print(f"O numero 5 não encontrado")