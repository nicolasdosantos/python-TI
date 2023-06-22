# NOME: NICOLAS - QUESTÃO: CONTA


teste = int(input("Bem vindo ao programa, quantas vezes voce de vai querer teste?\n"))

for i in range(teste):
    pergunta = int(input("Quantas vezes voce e seu amigo iram querer de termos para indicar a somatoria?\n"))
    if pergunta %2 == 0:
        print(f"O resultado da somatoria de {pergunta} termos foi de 0")
    else:
        print(f"O resultado da somatoria de {pergunta} foi de 1")