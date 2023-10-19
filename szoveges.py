print('ja' + 'j' * 7)

sztring = 'Ismered ezt a számot?'

print(sztring[2:11])
print(sztring[:9])
print(sztring[7:])

szamlalo = 0
for betu in sztring:
    if betu == 'e' or betu == 'E':
        szamlalo += 1
print(f'A sztringben {szamlalo} db e/E betű van.')

if 'e' in sztring:
    print('Van benne e betű.')
else:
    print('Nincs benne e betű.')

sztring = 'Ismered ezt a számot?'
sztring = 'i' + sztring[1:]
print(sztring)