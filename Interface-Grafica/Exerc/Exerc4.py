import customtkinter as tk

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


def soma():
    caul = int(caixa1.get()) + int(caixa2.get())
    texto1.configure(text=f"O resultado da soma é, {caul}")

def sub():
    caul = int(caixa1.get()) - int(caixa2.get())
    texto1.configure(text=f"O resultado da subtração é, {caul}")

def mult():
    caul = int(caixa1.get()) * int(caixa2.get())
    texto1.configure(text=f"O resultado da multiplicação é, {caul}")

def div():
    caul = int(caixa1.get()) / int(caixa2.get())
    texto1.configure(text=f"O resultado da divisão é, {caul}")

soma= tk.CTkButton(janela, text="+", command=soma, width=50, height=30,fg_color="black")
soma.grid(row=7,column=5)

sub= tk.CTkButton(janela, text="-", command=sub, width=50, height=30,fg_color="black")
sub.grid(row=7,column=6)

mult= tk.CTkButton(janela, text="*", command=mult, width=50, height=30,fg_color="black")
mult.grid(row=7,column=7)

div= tk.CTkButton(janela, text="/", command=div, width=50, height=30,fg_color="black")
div.grid(row=7,column=8)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite o primeiro numero", width=200, height=30)
caixa1.grid(row=5, column=5, columnspan=4)

caixa2 = tk.CTkEntry(janela, placeholder_text="Digite o segundo numero", width=200, height=30)
caixa2.grid(row=6, column=5, columnspan=4)


janela.mainloop()