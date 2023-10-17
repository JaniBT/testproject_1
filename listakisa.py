kisalista = []

print("Kis vagy nagy A betűvel kezdődő szavakat tárol el a program egy listában (ENTER leütésével léphetsz ki!).\n")

igaz = True
while igaz:
    szo = input("Adj meg szavakat: ")
    if szo == "":
        igaz = False
    elif szo[0].lower() == "a":
        kisalista.append(szo)

print(*kisalista)