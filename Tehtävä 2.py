import string

nimet = {"alku"}
nimet.remove("alku")
while True:
    nimi = input('Anna nimi ')
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(nimi)
list1 = list(nimet)
a = 0
b = len(nimet)
for i in range(b):
    print(list1[a])
    a = a + 1

