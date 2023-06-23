#fruta = ["maca", "banana", "abacaxi", "uva"]
#print(fruta)
#fruta[3] = "melancia"
#print(fruta)
#fruta.append("goiaba")
#print(fruta)
#fruta.insert(0, "morango")
#print(fruta)
#fruta.insert(1, "pera")
#print(fruta)
#del fruta[0]
#print(fruta)
#if "abacaxi" in fruta:
#    fruta.remove("abacaxi")
#    print(fruta)
#else:
#    print("Não encontrado")

#num = [6,5,7,3,6,8,9,0]
#num.sort()
#print(num)
#num.sort(reverse=True)
#print(num)
#soma = sum(num)
#print(f"Soma: {soma}")
#maior = max(num)
#menor = min(num)
#print(f"Menor: {menor}")
#print(f"Maior: {maior}")

#fruta = ["maca", "banana", "abacaxi", "uva"]
#maior = max(fruta, key=len)
#print(f"Maior: {maior}")
#menor = min(fruta, key=len)
#print(f"Menor: {menor}")

num1 = [6,5,7,3,6,8,9,0]
num2 = num1
num2[1] = 2
print(f"Num1: {num1}")
print(f"Num2: {num2}")

num1 = [6,5,7,3,6,8,9,0]
num2 = num1[:]
num2[1] = 2
print(f"Num1: {num1}")
print(f"Num2: {num2}")

num1 = []

while True:
    num1.append(int(input("Digite um numero")))
