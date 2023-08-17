import calculadora

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

op = str(input("Qual operação voce ira usar?\nAdição(+)\nSubtração(-)\nMultiplicação(*)\nDivisão(/)\n"))

if op == "+":
    print(calculadora.soma(num1, num2))
elif op == "-":
    print(calculadora.subtracao(num1, num2))
elif op == "*":
    print(calculadora.multiplicacao(num1, num2))
elif op == "/":
    print(calculadora.divisao(num1, num2))