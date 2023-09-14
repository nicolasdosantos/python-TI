import customtkinter as tk
bol = 0
lula = 0

tk.set_appearance_mode("Dark")

janela = tk.CTk()
janela.title("Janela")
janela.geometry("400x350")
janela.configure(fg_color="#94d2bd")
janela.resizable(width=False, height=False)

colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)


texto1 = tk.CTkLabel(janela, text="Os numeros dos eleitores são , 13(Faz o L) e 17!",text_color="Black", font=("Arial",16),justify="center")
texto1.grid(row=3,column=6)

texto2 = tk.CTkLabel(janela, text="Digite 0 para sair",text_color="Black", font=("Arial",16),justify="center")
texto2.grid(row=4,column=6)

def clique():
    global bol
    global lula

    voto = int(caixa1.get())
    if voto == 17:
        bol += 1
        texto1.configure(text=f"Voto feito com sucesso")
    elif voto == 13:
        lula += 1
        texto1.configure(text=f"Voto feito com sucesso")
    elif voto == 0:
        texto1.configure(text=f"Os votos totais foram de {bol} para bolsonaro")
        texto2.configure(text=f"Os votos totais foram de {lula} para Lula")
    else:
        texto1.configure(text=f"O numero desse eleitor não existe")


btn1 = tk.CTkButton(janela, text="Enviar voto", command=clique, width=50, height=30, fg_color="Black")
btn1.grid(row=7,column=6)


caixa1 = tk.CTkEntry(janela, placeholder_text="Digite o numero do seu elitor", width=200, height=30)
caixa1.grid(row=5, column=5, columnspan=4)


janela.mainloop()