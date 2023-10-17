import random

szamok = []

for _ in range(10):
    szam = random.randint(1, 50)
    if szam % 4 == 0:
        szamok.append(szam)

print(*szamok)
print(f'Összesen ennyi szám van: {len(szamok)}')