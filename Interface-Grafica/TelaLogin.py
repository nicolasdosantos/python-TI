import customtkinter as tk
from Modulo import *

tk.set_appearance_mode("Light")
tk.set_default_color_theme("themes/violet.json")
def Clique():
    var1 = input1.get()
    var2 = input2.get()
    if var1 not in login.keys():
        texto2 = CriarLabel(janela, "Login / Senha incorretos", 4, 0)
        texto2.grid(columnspan=12)
        texto2.configure(text_color="Red", font=("Arial", 16))

    elif var1 in login.keys():
        texto2 = CriarLabel(janela, "Login feito com sucesso", 4, 0)
        texto2.grid(columnspan=12)
        texto2.configure(text_color="Green", font=("Arial", 16))

    if var2 not in login.values():
        texto2 = CriarLabel(janela, "Login / Senha incorretos", 4, 0)
        texto2.grid(columnspan=12)
        texto2.configure(text_color="Red", font=("Arial", 16))

    elif var2 in login.values():
        texto2 = CriarLabel(janela, "Login feito com sucesso", 4, 0)
        texto2.grid(columnspan=12)
        texto2.configure(text_color="Green", font=("Arial", 16))


login = {"Nicolas": "12345", "Miguel": "12345", "Henri": "12345", "Basinga": "12345", "Muliro": "12345", "Lara": "12345"}



janela = CriarJanela("Janela", "400x350", 1)
texto1 = CriarLabel(janela, "LOGIN", 2, 0)
texto1.grid(columnspan=12)
texto1.configure(text_color="Black", font=("Arial",30))
input1 = CriarInput(janela,Largura=200, Altura=30, Linha=5, Coluna=6, Texto="Insira seu nome")
input2 = CriarInput(janela,Largura=200, Altura=30, Linha=6, Coluna=6, Texto="Insira sua senha")
input2.configure(show="*")
check = CriarCheck(janela,"Lembre de Mim", 7,6)
check.configure(text_color="Black", font=("Arial", 16))
check.get()
btn1 = CriarBotao(janela, Texto="LOGIN", Comando=Clique , Linha=8, Coluna=6, Largura=195, Altura=30)


janela.mainloop()