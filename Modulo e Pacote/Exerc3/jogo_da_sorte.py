import random

num = random.randint(1, 100)

chanche = 5


while chanche > 0:
    print(f"Voce tem {chanche} chanches restantes")
    p = int(input("Digite um numero para adivinhar:\n"))
    chanche -= 1
    if p < num:
        print("O numero é maior, tente outra vez")
    elif p > num:
        print("O numero é menor, tente outra vez")
    elif p == num:
        print(f"PARABENS VOCE ACERTOU O NUMERO!!, ELE ERA {num}")
        break

print(f"Voce perdeu, o numero certo era {num}")
