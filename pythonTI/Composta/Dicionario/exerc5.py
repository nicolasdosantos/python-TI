notas = {}

while True:
    n = int(input("Digite um instrumento avaliativo\n"))
    notas[n] = float(input("Digite sua nota da avaliação\n"))
    p = str(input("Voce deseja continuar?S ou N")).lower()

    if p == "n":
        break

nota = notas.values()
nota = list(nota)

med = sum(nota)
med = med / len(nota)
print(med)