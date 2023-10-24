autók = [['ABCD-12', 64], ['DBBA-17', 45], ['DDCD-72', 57], ['EGHI-49', 50], ['TRUM-73', 60]]

print('Az első autó sebessége: ', autók[0][1], ' km/h')

print(f'Az utolsó autó rendszáma: {autók[-1][0]}')

print(f'A rögzített autók száma: {len(autók)}')

sebessegek = list()
for auto in autók:
    sebessegek.append(auto[1])
    
print(f'Az autók sebessége az áthaladás sorrendje szerint: {sebessegek}')

print('Gyorsabbak, mint 50 km/h: ', end=' ')
for autó in autók:
    if autó[1] > 50:
        print(autó[0], end=' ')
        
rendszamok = []