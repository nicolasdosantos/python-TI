itens = ("Fruta - 0", "Jogo - 1","Caneta - 2", "Bolsa - 3")
f = ("Fruta: Goiaba, Quantidade: 15, Preço: 10,99Kg")
j = ("Jogo: Overcooked, Quantidade: 10, Preço: 60,00")
c = ("Marca: Bic, Quantidade: 6, Preço: 02,00")
b = ("Marca: kipling, Quantidade: 1, Preço: 800,00")
p = int(input("Qual Item voce quer as informações"))

if p == 0:
    print(f)
elif p == 1:
    print(j)
elif p == 2:
    print(c)
elif p == 3:
    print(b)