szavak = []

szo = input('Adj meg egy szót: ')

while szo != '':
    szavak.append(szo)
    szo = input('Adj meg egy szót: ')

print(szavak)

legrovidebb = min(szavak, key=len)
leghosszabb = max(szavak, key=len)

print(f'A legrövidebb szó: {legrovidebb}')
print(f'A leghosszabb szó: {leghosszabb}')