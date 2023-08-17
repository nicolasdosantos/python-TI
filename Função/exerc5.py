def ficha(nome="", gol=0):
    print(f"O jogador {nome} marcou {gol} gols")


n = str(input("Digite o nome do jogador:\n"))
i = int(input("Digite a quantidade de gols:\n"))
ficha(n,i)