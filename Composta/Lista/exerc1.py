num = []
while True:
    num.append(int(input(f"Digite um numero inteiro\n")))
    res = int(input(f"Digite 0 para sair e 1 para continuar\n"))
    if res == 0:
        print("Voce esta encerrando o programa")
        print(f"Aqui esta a soma do seus numeros: {sum(num)}")
        print(f"Aqui esta o maior dos digitado por voce: {max(num)}")
        print(f"Aqui esta o menor dos digitado por voce: {min(num)}")
        break
multi = 1

for i in num:
    multi = multi * i
print(f"A multiplicação desses numeros são {multi}")