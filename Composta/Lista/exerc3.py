num = []

p = int(input("Quantas vezes voce ira querer testar o programa?\n"))

for i in range(p):
    num.append(int(input("Digite um numero inteiro\n")))

soma = sum(num)
menor = min(num)
print(f"A soma dos numeros digitados é de: {soma}\nO menor numero inserido é o: {menor}")