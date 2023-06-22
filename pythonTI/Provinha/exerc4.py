#NOME: Nicolas - QUESTÃO: Figurinha

# INPUT PARA SABER A QUANTIDADE DE REPETIÇÃO
teste = int(input("Quantas vezes voce ira testar o programa?"))

# FOR PARA FZR A REPETIÇÃO
for i in range(teste):
    # CRIAÇÃO DAS VARIAVEIS
    num1 = int(input("Digite seu primeiro numero inteiro"))
    num2 = int(input("Digite seu segundo numero inteiro"))

    #SE O NUMERO POR PAR, ELE IRA PEGAR O RESTO DA DIVISÃO DO NUMERO 2 PELO 1, E O RESTO DA DIVISÃO SERA O DIVISOR DOS DOIS
    if num1 %2 == 0:
        print(f"O MDC dos numero {num1} e {num2}, é {num2 % num1}")
    #SE O NUMERO POR IMPAR, ELE IRA PEGAR O RESTO DA DIVISÃO DO NUMERO 1 PELO 2, E O RESTO DA DIVISÃO SERA O DIVISOR DOS DOIS
    else:
        print(f"O MDC dos numero {num1} e {num2}, é {num1 % num2}")