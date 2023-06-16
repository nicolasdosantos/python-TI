cardapio = ("Hamburguer - 1", "Pizza - 2", "Batata Frita - 3", "Frios - 4")
print(cardapio)
pedido = int(input("Qual sera a quantidade de pedidos?max:3"))
if pedido == 1:
    print(cardapio)
    int(input("Qual sera seu pedido?"))
elif pedido == 2:
    print(cardapio)
    for i in range(2):
     int(input("Qual sera seu pedido?"))
elif pedido == 3:
    int(input("Qual sera seu pedido?"))
    for i in range(3):
        int(input("Qual sera seu pedido?"))