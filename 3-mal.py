# szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]

# for szam in szamok:
#     if szam % 3 == 0:
#         if szam % 2 == 0:
#             print(f'\b{szam}')



szamok = []

szam = 0

for _ in range(40):
    szam += 1
    if szam % 3 == 0:
        szamok.append(szam)

print(*szamok)