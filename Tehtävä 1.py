
vuodenajat = {'Kevät' : (1,2,3), 'Kesä' : (4,5,6), "Syksy" : (7,8,9), "Talvi" : (10,11,12)}
kuunum = int(input("Anna kuukauden numero "))

if kuunum in vuodenajat['Kevät']:
    print("Kevät")
if kuunum in vuodenajat['Kesä']:
        print("Kesä")
if kuunum in vuodenajat['Syksy']:
            print("Syksy")
if kuunum in vuodenajat['Talvi']:
    print("Talvi")



