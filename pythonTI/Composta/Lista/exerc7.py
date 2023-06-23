num = []

p = int(input("Quantas vezes voce ira testas o programa?\n"))

for i in range(p):
    x = int(input("Digite algum numero\n"))
    if x == 0:
        break
    elif x not in num:
        num.append(x)
num.sort()
print(num)