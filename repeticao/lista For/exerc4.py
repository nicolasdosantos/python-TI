max = 50
cliente = 0
for i in range(max+1):
    clientes = int(input("Quantos clientes já entraram até agora?: "))
    cliente = clientes
    if max <= cliente:
        print("«Restaurante lotado, não há mais mesas disponíveis»")
#        max -= cliente
        break
    else:
        print(f"Ainda temos lugar no restaurante, a capaxidade esta em")