import customtkinter as tk
import statistics

tk.set_appearance_mode("Dark")

janela = tk.CTk()
janela.title("Janela")
janela.geometry("500x450")
janela.configure(fg_color="#94d2bd")
janela.resizable(width=False, height=False)

colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)


texto1 = tk.CTkLabel(janela, text="",text_color="Black", font=("Arial",16),justify="center")
texto1.grid(row=4,column=1, columnspan=12)

lista = []

def adicionar():
    num = int(caixa1.get())
    lista.append(int(num))

def media():
    valor = statistics.mean(lista)
    texto1.configure(text=f"A media dos valores é, {valor}")


def moda():
    valor = statistics.mode(lista)
    texto1.configure(text=f"A moda dos valores é, {valor}")

def mediana():
    valor = statistics.median(lista)
    texto1.configure(text=f"A mediana dos valores é, {valor}")

add= tk.CTkButton(janela, text="Enviar", command=adicionar, width=50, height=30,fg_color="black")
add.grid(row=7,column=5)

media= tk.CTkButton(janela, text="Media", command=media, width=50, height=30,fg_color="black")
media.grid(row=7,column=6)

moda= tk.CTkButton(janela, text="Moda", command=moda, width=50, height=30,fg_color="black")
moda.grid(row=7,column=7)

mediana= tk.CTkButton(janela, text="Mediana", command=mediana, width=50, height=30,fg_color="black")
mediana.grid(row=7,column=8)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite o primeiro numero", width=200, height=30)
caixa1.grid(row=5, column=5, columnspan=4)


janela.mainloop()