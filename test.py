#n = int(input("Digite um numero\n"))

#if n == 1:
#    print("Amarelo")
#elif n == 2:
#    print("Azul")
#elif n == 3:
#    print("Verde")
#else:
#    print("Sem cor")


#match n:
#    case 1:
#        print("Amarelo")
#    case 2:
#        print("Azul")
#    case 3:
#        print("Verde")
#    case _:
#        print("Sem cor")



login = str(input("Digite seu login\n"))
senha = str(input("Digite sua senha\n"))

match (login,senha):
    case("Bruno", "123"):
        print("Logado com sucesso")
    case _:
        print("Login ou senha incorreta")