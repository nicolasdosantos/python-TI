NomeV = "n"
idadeV = 0
qMulher = 0

for i in range(3):
    g = int(input("Qual é seu genero?\nFeminino(1)\nMasculino(2)"))
    if g == 2:
        nome = input("Qual seu nome?")
        idade = int(input("Qual sua idade?"))
        if idade > idadeV:
            NomeV = nome
            idadeV = idade
    elif g == 1:
        nome = input("Qual seu nome?")
        idade = int(input("Qual sua idade?"))
        if idade < 20:
            qMulher += 1
print(f"O homem mais velho é {NomeV}\nO numero de mulheres com menos de 20 anos é de {qMulher}")