import customtkinter as tk
from Modulo import *


def clicar():
    pass


janela = CriarJanela("Janela", "400x350", 1)
text = CriarLabel(janela, "Revisão", 3, 6)
btn = CriarBotao(janela,"Clique aqui", clicar, 9, 9, 5, 6)


janela.mainloop()