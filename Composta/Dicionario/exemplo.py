d = {}

while True:
    chave = str(input("Digite um elemento\n"))
    d[chave] = str(input("Digite um valor para o elemento\n"))
    p = str(input("Desejar continuar?S ou N")).lower()
    if p == "n":
        print(f"Seu dicionario ficou assim: {d}")
        break