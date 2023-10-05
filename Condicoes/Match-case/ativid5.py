login = str(input("Digite seu login\n")).lower()
senha = str(input("Senha sua senha\n")).lower()

match (login,senha):
    case ("admin", "admin_pass"):
        print("Voce esta logando como adm")
    case ("user", "user_pass"):
        print("Voce esta logando como usuario")
    case ("guest", _):
        print("Voce esta logando como tester")