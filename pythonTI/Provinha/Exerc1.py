# NOME: NICOLAS - ATIVIDADE: BATMAIN

# PROGRAMAÇÃO PARA AJUDAR NOSSO COLOGUINHA BATMAIN E SALVAR A CIDADE DO CRIME

# ENTRADA PARA VERIICAR QUANTAS VEZES ELE IRÁ QUERER USAR O TESTE
teste = int(input("Olá caro cavalheiro das trevas, estou aqui para de ajudar a ver quantas vezes voce já capturou um prisioneiro. Digite para mim quantas vezes voce ira verificar os prisioneiro\n"))

# AQUI ESTÃO AS VARIAVEIS DE VILÕES QUE FORAM ADICIONADAS NO PROGRAMA E A QUANTIDADE DE VEZES QUE ELE FOI CAPTURADO
coringa = 3
pistoleiro = 5
pinguin = 16
charada = 10
thanos = 0

# AQUI É ONDE COMEÇAR O LOOPING PARA VERIFICAR OS VILOES
for i in range(teste):

    # AQUI TEMOS A PERGUNTA EM FORMATO DE STRING PARA SABER QUAL VILÃO SERÁ VERIFICADO
    vilao = str(input("Então vamos seguir. Qual vilão você gostaria de analisar?Digite o numero 0 para sair antes do desejado ou ocorra algo inesperado\n")).lower()

    # A PARTIR DAQUI TEMOS A VERIFICAÇÃO E O PRINT COM A INFORMAÇÃO SE ELE JA FOI OU NÃO CAPTURADO
    if vilao == "coringa":
        print(f"O vilão escolido foi o {vilao}, até onde meus dados indicam e foram atualizados você já capturou ele meu heroi, e foram um total de {coringa} vezes\n")
    elif vilao == "pistoleiro":
        print(f"O vilão escolido foi o {vilao}, até onde meus dados indicam e foram atualizados você já capturou ele meu heroi, e foram um total de {pistoleiro} vezes\n")
    elif vilao == "pinguin":
        print(f"O vilão escolido foi o {vilao}, até onde meus dados indicam e foram atualizados você já capturou ele meu heroi, e foram um total de {pinguin} vezes\n")
    elif vilao == "charada":
        print(f"O vilão escolido foi o {vilao}, até onde meus dados indicam e foram atualizados você já capturou ele meu heroi, e foram um total de {charada} vezes\n")
    elif vilao == "thanos":
        print(f"Meu cavalheiro das trevas, voce esta indo para outros universos caçar vilão?{vilao}, ainda não foi capturado nenhuma vez\n")
    elif vilao == "0":
        print(f"Saindo do programa, até breve cavalheiro das trevas\n")
        break
    else:
        print(f"Verifique se voce digitou o nome certo caro heroi, esse vilão não consta no meu banco de dados\n")

# A PARTIR DAQUI É UM ALGO A MAIS ;), O QUE A QUESTÃO PEDI ESTA A CIMA

c = str(input("Todas as verificações que você desejava foram feitas, você gostaria de atualizar o programa?")).lower()

if c == "sim":
    vilao2 = str(input("Qual vilão você gostaria de atualizar?Digite 0 para sair\n"))
    if vilao2 == "coringa":
        q = int(input(f"Quantas vezes você capturou a mais o {vilao2}? o numero atual é de {coringa}\n"))
        coringa += q
    elif vilao2 == "thanos":
        q = int(input(f"Quantas vezes você capturou a mais o {vilao2}? o numero atual é de {thanos}\n"))
        thanos += q
    elif vilao2 == "pinguin":
        q = int(input(f"Quantas vezes você capturou a mais o {vilao2}? o numero atual é de {coringa}\n"))
        pinguin += q
    elif vilao2 == "charada":
        q = int(input(f"Quantas vezes você capturou a mais o {vilao2}? o numero atual é de {charada}\n"))
        charada += q
    elif vilao2 == "pistoleiro":
        q = int(input(f"Quantas vezes você capturou a mais o {vilao2}? o numero atual é de {pistoleiro}\n"))
        pistoleiro += q
    elif vilao2 == "0":
        print("Saindo do programa\n")
        break
else:
    print("Então acho que por hoje é só meu heroi até a proxima")