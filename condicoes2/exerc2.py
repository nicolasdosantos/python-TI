c = int(input("Coloquei o valor da compra"))
p = int(input("Coloque em quantas prestações será pago"))
calculo = c/p
if calculo > 500:
    print(f"Você não conseguira pagar, pois cada prestação ficou {calculo}")
elif calculo < 500:
    print("Você conseguira pagar")
elif calculo == 500:
    print("Você paraga por pouco tome cuidado!!")