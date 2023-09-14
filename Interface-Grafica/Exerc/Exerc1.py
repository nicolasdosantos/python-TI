import customtkinter as tk

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


texto1 = tk.CTkLabel(janela, text="",text_color="Black", font=("Arial",16),justify="center")
texto1.grid(row=4,column=6)


def clique():
    nota = int(caixa1.get()) + int(caixa2.get())

    if nota >= 6:
        texto1.configure(text=f"Esse aluno foi aprovado")
    elif nota < 6:
        texto1.configure(text=f"O aluno foi reprovado")


btn1 = tk.CTkButton(janela, text="Clique Aqui", command=clique, width=50, height=30)
btn1.grid(row=7,column=6)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite a primeira nota", width=200, height=30)
caixa1.grid(row=5, column=6)

caixa2 = tk.CTkEntry(janela, placeholder_text="Digite a segunda nota", width=200, height=30)
caixa2.grid(row=6, column=6)


janela.mainloop()