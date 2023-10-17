szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
szav = []

for szo in szavak:
    if szo.startswith('t') or szo.startswith('T'):
        szav.append(szo)

print(*szav)