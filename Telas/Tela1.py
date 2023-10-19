from Modulos import *
import customtkinter as Tk


def MostrarTela1():
    Janela.deiconify()


def AbrirTela2():
    from Tela2 import MostrarTela2
    Janela.withdraw()
    MostrarTela2()


Janela = CriarJanela("Janela","400x400",1)
Nome_Tela1 = CriarLabel(Janela,"Tela Inicial",2,6)
Fr_Tela1 = CriarFrame(Janela,4,0,300,300)
Fr_Tela1.grid(columnspan=13)
Texto_Tela1= CriarLabel(Fr_Tela1,"🌟 Bem-vindo(a) ao processo de cadastro! 🌟 \n\n\n "
                                 "Estamos entusiasmados por tê-lo(a) conosco.\n Ao completar o seu cadastro,"
                                 " você terá acesso\n completo a todas as funcionalidades e recursos\n que nossa plataforma oferece.",4,6)
Btn_Ir = CriarBotão(Janela,"Proxima tela",AbrirTela2,7,0,200,30)
Btn_Ir.grid(columnspan=13)

Janela.mainloop()