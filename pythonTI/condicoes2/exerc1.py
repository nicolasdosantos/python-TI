time1 = int(input("Coloquei seu placar do primeiro time"))
time2 = int(input("Coloquei seu placar do segundo time"))

if time1 == time2:
    print("A partida terminou em empate")
elif time1 > time2:
    print("A vitoria é do time 1")
elif time1 < time2:
    print("A vitoria é do time 2")