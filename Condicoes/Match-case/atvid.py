n = int(input("Digite um numero\n"))

match n:
    case 1:
        print("Voce digitou 1")
    case 2:
        print("Voce digitou 2")
    case 3:
        print("Voce digitou 3")
    case _:
        print("Voce digitou errado")