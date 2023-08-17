caro = ""
valorM = 0
p = "S"
while True:
    prod = str(input("Qual é o nome do produto?: "))
    valor = int(input("Qual é o valor dele?: "))
    p = str(input("Voce quer continuar?(S ou N): "))
    valorM += valor
    if valor > valorM:
        caro = prod
    if p == "N":
        print("Muito obrigado pela compra")
        print(f"Sua compra no total foi de {valorM} e seu produto mais caro foi o {caro}")
        break