time1 = int(input("Coloquei seu placar do primeiro time"))
time2 = int(input("Coloquei seu placar do segundo time"))
if time1 == time2:
    print(f"A partida terminou em empate com o resultado de {time1}x{time2}")
elif time1 > time2:
    print(f"A vitoria é do time 1 com o placar de {time1}x{time2}")
elif time1 < time2:
    print(f"A vitoria é do time 2 com o placar de {time1}x{time2}")