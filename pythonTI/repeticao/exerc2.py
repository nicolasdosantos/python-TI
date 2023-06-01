cliente = input("Informe a quantidade de cliente")
soma = 0
for i in range(1, cliente+1):
    t = int(input("Informe sua temperatura"))
    soma += t
    if t < 37.2:
        print("Sua temperatura esta normal")
    elif 37.3>=t<38:
        print("Sua temperatura esta em estado febril")
    elif 38>=t<39:
        print("Voce esta com febre")
    elif t > 39:
        print("Sua temperatura esta com febre alta")
media = soma/cliente
print(f"A media de temperatura é de {media} e a quantidade de cliente é de {cliente}")

