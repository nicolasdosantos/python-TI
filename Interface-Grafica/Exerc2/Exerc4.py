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


qnt = 0
lista = []



texto1 = tk.CTkLabel(janela, text=f"O total de numeros digitados é de {qnt}",text_color="Black", font=("Arial",16),justify="center")
texto1.grid(row=3,column=6)

texto2 = tk.CTkLabel(janela, text=f"",text_color="Black", font=("Arial",16),justify="center")
texto2.grid(row=4,column=6)


def clique():
    global lista
    valor = int(caixa1.get())
    lista.append(valor)
    lista.sort(reverse=True)
    texto3 = tk.CTkLabel(janela, text=f"lista: {lista}", text_color="Black", font=("Arial", 16), justify="center")
    texto3.grid(row=2, column=6)
    if valor == 5:
        texto1.configure(text=f"O numero 5 foi digitado")


btn1 = tk.CTkButton(janela, text="Clique Aqui", command=clique, width=50, height=30)
btn1.grid(row=7,column=6)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite a primeira nota", width=200, height=30)
caixa1.grid(row=5, column=6)



janela.mainloop()