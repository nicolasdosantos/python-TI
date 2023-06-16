fruta = ("Maça", "Banana", "Abacaxi", "Uva")
fruta2 = ("Laranja", "Moranga", "Melancia")
fruta3 = fruta + fruta2

#Um elemento expecifico
print(fruta3[4])

#Vai imprimir do 0 até o 4
print(fruta3[0:4])

#Vai imprimir até o final
print(fruta3[1:])

#Vai imprimir o ultimo
print(fruta3[-1])

#Me fala quantos elementos tem nessa lista
print(len(fruta3))

#Ordem alfabetica
print(sorted(fruta3))

#Me mostra a posição da primeira variavel com esse nome
print(fruta3.index("Banana"))

#Conta quantas bananas tem na lista ou tupla
print(fruta3.count("Banana"))

#Deleta a lista
del (fruta3)