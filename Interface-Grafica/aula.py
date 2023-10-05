import customtkinter as tk
from Modulo import *

janela = CriarJanela("Janela", "400x350", 1)
janela2 = CriarJanela("Janela2", "400x350", 2)
janela2.withdraw()
texto1 = CriarLabel(janela, "", 6, 6)
texto1.configure(text_color="Black", font=("Arial",16),justify="center")



def clique():
    janela2.deiconify()
    texto1.configure(text=caixa1.get())



btn1 = tk.CTkButton(janela, text="Clique Aqui", command=clique, width=50, height=30)
btn1.grid(row=8,column=6)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite seu nome", width=200, height=30)
caixa1.grid(row=7, column=6)



janela.mainloop()