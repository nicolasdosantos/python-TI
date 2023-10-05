a = str(input("Digite um Animal(Vaca,Galinha,Ovelha)\n")).lower()


match a:
    case ("vaca"):
        print("Vaca foi sua escolha")
    case ("galinha"):
        print("Galinha foi sua escolha")
    case ("ovelha"):
        print("Ovelha foi sua escolha")
    case _:
        print("Animal desconhecido")