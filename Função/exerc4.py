def voto(ano):
    ano = 2023 - ano
    if ano < 16:
        print("Voce não pode votar")
    elif ano >= 16 and ano < 18:
        print("Voce tem o voto opicional")
    elif ano >=18:
        print("Voce tem o voto obrigatorio")


a = int(input("Digite seu ano de nacimento:\n"))
voto(a)