# NOME: Nicolas - QUESTÃO: Ultimo Anagolimon

# AQUI É A CRIÇÃO DE VARIAVEIS
tempo = 0
linha2 = 0
coluna2 = 0

# APRESENTAÇÃO DO JOGO
print("Bem-Vindo ao caça pokemon em python, vamos começar a jogatina\n")

print("Voce esta na posição 0 da cidade sendo a cidade um quadrado de 5x5, então voce esta na posição 0x0, Sendo assim vamos lá")

# AQUI É ONDE COMEÇA O WHILE
while True:
    # PERGUNTA PARA SABER A DIREÇÃO
    pergunta = str(input("Para qual direção voce ira andar, voce só pode andar 1 bloco por vez\nDireita(d)\nCima(c)\nEsquerda(e)\nBaixo(b)\nDigite 0 para sair")).lower()
    if pergunta == "d":
        # SE ELE FOR PARA DIREITA ELE AUMENTA 1 EM LINHA E CRONOMETRA O TEMPO
        linha2 += 1
        tempo += 1
        print(f"Voce andou 1 quadrado para a direita,voce esta na linha {linha2} da coluna {coluna2}")
    if pergunta == "e":
        # SE ELE FOR PARA ESQUERDA ELE DIMINUI 1 EM LINHA E CRONOMETRA O TEMPO
        linha2 -= 1
        tempo += 1
        print(f"Voce andou 1 quadrado para a esquerda,voce esta na linha {linha2} da coluna {coluna2}")
    if pergunta == "c":
        # SE ELE FOR PARA CIMA ELE AUMENTA 1 EM COLUNA E CRONOMETRA O TEMPO
        coluna2 += 1
        tempo += 1
        print(f"Voce andou 1 quadrado para a cima,voce esta na linha {linha2} da coluna {coluna2}")
    if pergunta == "b":
        # SE ELE FOR PARA CIMA ELE DIMINUI 1 EM COLUNA E CRONOMETRA O TEMPO
        coluna2 -= 1
        tempo += 1
        print(f"Voce andou 1 quadrado para a baixo,voce esta na linha {linha2} da coluna {coluna2}")
    if pergunta == "0":
        print(f"Voce esta saindo do programa!!")
        break
    elif linha2 == 3 and coluna2 == 3:
        # AQUI VERIFICA SE VOCE GANHOU OU NÃO
        print(f"PARABENS!! Você achou o pokemon, o menor tempo para fazer essa caçada é de 6 segundos e voce fez em exatos {tempo}")