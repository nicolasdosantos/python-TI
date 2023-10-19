from Modulos import *
import customtkinter as Tk


def MostrarTela2():
    Janela2.deiconify()


def AbrirTela1():
    Janela2.withdraw()
    from Tela1 import MostrarTela1
    MostrarTela1()

Janela2 = CriarJanela("Janela 2","400x400",2)
Janela2.withdraw()
Nome_Tela2 = CriarLabel(Janela2,"Tela de Cadastro",2,6)
Fr_Tela2 = CriarFrame(Janela2,4,0,300,300)
Fr_Tela2.grid(columnspan=13)
Img_Tela2 = CriarImagem(Fr_Tela2,"Imagens/construcao.png",6,6,200,200)
Btn_Voltar = CriarBotão(Janela2,"Voltar",AbrirTela1,7,0,200,30)
Btn_Voltar.grid(columnspan=13)