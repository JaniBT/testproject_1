tancosok = [['Katalin', 'Ede'], ['Olga','Olivér',], ['Éva', 'Ádám'], ['Bea','Béla'], ['Anna', 'Pál']]

print(tancosok[0][1])

print(tancosok[-1][0])

print(len(tancosok))

lanytancosok = []

for lany in tancosok:
    lanytancosok.append(lany[0])

print(lanytancosok)

fiuk = []

for fiu in tancosok:
    fiuk.append(fiu[1])

for par in tancosok:
    if par[0][0] == par[1][0]:
        print(par[0], par[1])