num = []

p = int(input("Quantas vezes voce ira testas o programa?\n"))

for i in range(p):
    num.append(int(input("Digite algum numero\n")))
    if num == num:
        print("Esse numero ja foi digitado")