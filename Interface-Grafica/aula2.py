import customtkinter as tk
from Modulo import *


def clique():
    if check.get() == 1:
        texto1.configure(text="Marcado")
    elif check.get() == 0:
        texto1.configure(text="Desmarcado")
    bar.set(0)

lista = ["Banana", "Maça","Goiaba", "Pera"]


janela = CriarJanela("Janela", "400x350", 1)
texto1 = CriarLabel(janela, "", 6, 6)
texto1.configure(text_color="Black", font=("Arial",16),justify="center")
input1 = CriarInput(janela,Largura=200, Altura=30, Linha=7, Coluna=6, Texto="Clique aqui")
btn1 = CriarBotao(janela, Texto="Clique aqui", Comando=clique , Linha=8, Coluna=6, Largura=50, Altura=30)
check = CriarCheck(janela,"Maque", 4,6)
check.get()
switch = CriarSwitch(janela, "Clique aqui", 4, 6)
box = CriarComboBox(janela, lista, Largura=200, Altura=30, Linha=5, Coluna=6)
bar = CriarBar(janela,Largura=200, Altura=10, Linha=10, Coluna=6)
slide = CriarSlider(janela,Largura=200, Altura=10, Linha=11, Coluna=6)


janela.mainloop()