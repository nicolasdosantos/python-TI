valor = int(input("Qual o valor?"))
taxa = int(input("Qual valor da taxa?"))
tempo = int(input("Qual é o tempo"))
prestacao = valor + (valor * (taxa/100) * tempo)
print(f"O valor da prestação é de {prestacao}")