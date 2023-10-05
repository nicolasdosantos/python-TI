d = str(input("Escreva seu dia da semana\n")).lower()

match d:
    case ("segunda"| "terça"| "quarta"| "quinta"|"sexta"):
        print(f"{d},  É um dia util")
    case ("sabado" | "Domingo"):
        print(f"{d}, É fim de semana")
    case _:
        print("Error")