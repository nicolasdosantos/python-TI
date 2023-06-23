#pessoa = {'nome':"duda", "idade":16, "altura": 1.50}
#print(pessoa["idade"])
#pessoa = {}

#pessoa["peso"] = 60.5

#del pessoa["peso"]

#pessoa = {'nome':"duda", "idade":16, "altura": 1.50}
#pessoa2 = {'nome':"brenda", "peso":60, "sexo": "f"}

#pessoa.update(pessoa2)
#pessoa2["peso"] = 52
#print(pessoa)
#print(pessoa2)

#pessoa = {'nome':"duda",
#          "idade":16,
#          "altura": 1.50}

#print(pessoa.keys())
#print(pessoa.values())
#print(pessoa.items())

#pessoa = {'nome':"duda", "idade":16, "altura": 1.50}

#for k,v in pessoa.items():
#    print(f"o item {k}, é {v}")

pessoa = {'nome':"duda", "idade":16, "altura": 1.50}

idade = int(input("Digite sua idade\n"))
if idade in pessoa.values():
    print("Voce tem a mesma idade")
