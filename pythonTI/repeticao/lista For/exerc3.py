eleitores = int(input("Quantos eleitores terão?"))
Bruno = 0
Igor = 0
Wellington = 0
for i in range(eleitores):
    votos = int(input("Temos 3 candidatos\nBruno(1) \nIgor(2) \nWellingthon(3)"))
    if votos == 1:
        Bruno += 1
    if votos == 2:
        Igor += 1
    if votos == 3:
        Wellington += 1
    print(f"Os votos ficaram de {Bruno} para o Bruno, {Igor} para o Igor e {Wellington} para o Wellingthon")