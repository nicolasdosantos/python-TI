#print("-----------")
#print("Senai legal")
#print("-----------")
#def linha():
#    print("-"*20)


#linha()
#print("Senai legal")
#linha()

#def linha(txt):
#    print("-"*20)
#    print(txt)
#    print("-"*20)


#linha("Senai legal")

#def soma(a,b):
#    s = a+b
#    print("A soma é", s)


#soma(234,645)
#soma(a=234,b=645)

#def soma(*valores):
#    s = 0
#    for c in valores:
#        s += c
#        print("A soma é", s)


#soma(178,1523,14)

#def soma(valores):
#    s = 0
#    for c in valores:
#        s += c
#        print("A soma é", s)


#num = [3,5,6,7,8,9,0,2,4,]
#soma(num)

#def soma(a,b=0):
#    s = a+b
#    print("A soma é", s)


#soma(1,300)
#soma(300)

#def soma(a,b=0):
#    s = a+b
#    return s


#a = soma(1,300)
#print("A soma é", a)

def ParOuImpar(num):
    if num %2 == 0:
        print("Seu numero é par")
    else:
        print("Seu numero é impar")


ParOuImpar(int(input("Digite um numero inteiro:\n")))