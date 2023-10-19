from Modulos import *
import customtkinter as Tk

def AbrirTela1():
    pass

Janela2 = CriarJanela("Janela 2","400x400",1)
Nome_Tela2 = CriarLabel(Janela2,"Tela de Cadastro",2,6)
Fr_Tela2 = CriarFrame(Janela2,4,0,300,300)
Fr_Tela2.grid(columnspan=13)
Img_Tela2 = CriarImagem(Fr_Tela2,"Imagens/construcao.png",6,6,200,200)
Btn_Voltar = CriarBotão(Janela2,"Voltar",AbrirTela1,7,0,200,30)
Btn_Voltar.grid(columnspan=13)
Janela2.mainloop()