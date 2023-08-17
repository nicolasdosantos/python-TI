nota = 0
media = 0
while True:
    notas = int(input('Digite sua nota '))
    nota += notas
    media += 1
    if media >=5:
        cal= nota/media
        print(f"Sua media é de {cal}")
        break