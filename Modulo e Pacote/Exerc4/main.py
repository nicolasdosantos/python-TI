import conversor_unidades

p = float(input("Digite os graus em Celsius\n"))

F = conversor_unidades.conversor_Fahrenheit(p)
K = conversor_unidades.conversor_Kelvin(p)

print(f"A temperatura em Celsius é, {p}")
print(f"A temperatura em Fahrenheit é, {F}")
print(f"A temperatura em Kelvin é, {K}")
