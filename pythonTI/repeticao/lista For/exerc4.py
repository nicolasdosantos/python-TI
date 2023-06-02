#depois pergunte e leia a quantidade de clientes que chegaram até ocupar toda a capacidade do restaurante e quando lotar imprima na tela «Restaurante lotado, não há mais mesas disponíveis».

max = 50
cliente = 0
for i in range(max):
    cliente = int(input("Quantos clientes já entraram até agora?: "))
    if cliente > max:
        print("«Restaurante lotado, não há mais mesas disponíveis»")
    else:
        print(f"Ainda temos lugar no restaurante, a capaxidade esta em {max-cliente}")