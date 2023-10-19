import customtkinter as tk
from Modulo import *

def clique():
    if check.get() == 1:
        texto1.configure(text="Marcado")
    elif check.get() == 0:
        texto1.configure(text="Desmarcado")
    bar.set(0)



janela = CriarJanela("Janela", "400x350", 1)
texto1 = CriarLabel(janela, "Name", 6, 6)
texto1.grid(stick = "SW")
texto1.configure(text_color="Black", font=("Arial",16),justify="center")
input1 = CriarInput(janela,Largura=200, Altura=30, Linha=7, Coluna=6, Texto="Clique aqui")
input1.grid(stick = "NW")
btn1 = CriarBotao(janela, Texto="Clique aqui", Comando=clique , Linha=8, Coluna=6, Largura=50, Altura=30)


janela.mainloop()