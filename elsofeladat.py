szamok = []
while True:
    bemenet = input("Kérem adjon meg egy számot ('X' vagy 'x' kiléphet): ")
    if bemenet.lower() == 'x':
        break
    try:
        szam = int(bemenet)
        szamok.append(szam)
    except ValueError:
        print("Hibás bemenet! Csak számokat fogadunk el.")

if szamok:
    print("A megadott számok:")
    for szam in szamok:
        print(szam)
    
    legnagyobb_szam = max(szamok)
    legkisebb_szam = min(szamok)
    
    print(f"A legkisebb szám: {legkisebb_szam}")
    print(f"A legnagyobb szám: {legnagyobb_szam}")
else:
    print("Nem adott meg egyetlen számot sem.")
