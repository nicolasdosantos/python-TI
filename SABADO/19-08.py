import mysql.connector

class contato():
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco


class agenda():
    def criarContato(self):
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        endereco = input("Digite o endereco: ")
        novoContato = contato(nome, telefone, email, endereco)
        return novoContato
    def inserir(self, nome, telefone, email, endereco):
        try:
            conexao = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="agenda")
            cursor = conexao.cursor()
            inserir = f"INSERT INTO AgendaTelefonica (nome, telefone, email, endereco) VALUES (%s, %s, %s, %s)"
            valores = (nome, telefone, email, endereco)
            cursor.execute(inserir, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(erro)


    def atualizar(self, id, nome, telefone, email, endereco):
        try:
            conexao = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="agenda")
            cursor = conexao.cursor()
            inserir = "UPDATE agendatelefonica SET nome = %s, telefone= %s, email= %s, endereco=%s WHERE id = %s;"
            valores = (nome, telefone, email, endereco, id)
            cursor.execute(inserir, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(erro)


    def deletar(self, id):
        try:
            conexao = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="agenda")
            cursor = conexao.cursor()
            inserir = f"DELETE FROM `agendatelefonica` WHERE id = %s;"
            valores = (id,)
            cursor.execute(inserir, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(erro)


    def mostrar(self, id):
        try:
            conexao = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="agenda")
            cursor = conexao.cursor()
            inserir = f"SELECT * FROM `agendatelefonica` WHERE id = %s;"
            valores = (id,)
            cursor.execute(inserir, valores)
            for (id, nome, telefone, email, endereco) in cursor:
                print(f"Id: {id} \nNome: {nome} \n",
                f"Tel: {telefone} \nEmail: {email}",
                f"\nEndereço: {endereco}")
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(erro)

def menu():
    while(True):
        print("1-Cadastrar")
        print("2-Apagar")
        print("3-Atualizar")
        print("4-Exibir")
        print("0-Sair\n")
        opcao = int(input("Digite a opção desejada"))
        if opcao == 1:
            cadastro = agenda2000.criarContato()
            agenda2000.inserir(cadastro.nome, cadastro.telefone, cadastro.email, cadastro.endereco)
        elif opcao == 2:
            id = int(input("Digite o Id: "))
            agenda2000.deletar(id)
        elif opcao == 3:
            id = int(input("Digite o Id para atualizar: "))
            nome = str(input("Digite o nome: "))
            telefone = str(input("Digite o telefone: "))
            email = str(input("Digite o email: "))
            endereco = str(input("Digite o endereco: "))
            agenda2000.atualizar(id, nome, telefone, email, endereco)
        elif opcao == 4:
            id = int(input("Digite o Id para exibir: "))
            agenda2000.mostrar(id)
        else:
            print("Opção invalida!")

agenda2000 = agenda()
menu()
#inserir(nome, telefone, email, endereco)
#atualizar(id, nome,telefone,email, endereco)