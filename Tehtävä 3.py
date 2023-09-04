lentkent: list[str] = []
while True:
    syotto = input("Haluatko syöttää- vai hakea lentokentän ")

    if syotto == "syöttää":
        icao = input("Annan ICAO ")
        kenttä = input("Anna nimi ")
        lentkent.append(icao)
        lentkent.append(kenttä)
    if syotto == "hakea":
        id = input('Anna kentän ICAO ')
        if id in lentkent:
            kentnimi = lentkent.index(id) + 1
            print("Lentokentän nimi on " + lentkent[kentnimi])
    if syotto == "Lopeta":
        break

