n = str(input("Digite uma Cor(Verde,Azul,Vermelho)\n")).lower()


match n:
    case ("vermelho"):
        print("Vermelho foi sua escolha")
    case ("verde"):
        print("Verde foi sua escolha")
    case ("azul"):
        print("Azul foi sua escolha")
    case _:
        print("Cor indefinida")
