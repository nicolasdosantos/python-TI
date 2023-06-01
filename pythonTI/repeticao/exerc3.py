from numpy.core.defchararray import lower, upper

mediaF = 0
mediaM = 0
mediaG = 0
idadeF = 0
idadeM = 0
idadeG = 0
for i in range(4):
    g = int(input("Qual é seu genero?\nFeminino(1)\nMasculino(2)"))
    if g == 1:
        idade = int(input("Qual é a sua idade?"))
        mediaG += 1
        mediaF += 1
        idadeF += idade
        idadeG += idade
    elif g == 2:
        idade = int(input("Qual é a sua idade?"))
        mediaG += 1
        mediaM += 1
        idadeM += idadeM
        idadeG += idade
calculoF = idadeF/mediaF
calculoM = idadeM/mediaM
calculoG = idadeG/mediaG
print(f"A media de idade entre as mulheres são{calculoF}\nA media de idade entre os homens é {calculoM}\nA media geral é {calculoG}")