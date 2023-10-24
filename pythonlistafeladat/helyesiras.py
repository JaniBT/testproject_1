szoveg = input('Adj meg egy szöveget! ')
irasjelek = '.,!?'

for index, betu in enumerate(szoveg):
    if betu in irasjelek:
        if szoveg[index-1] == ' ':
            print(f'Feleslegesen kitett szóköz {betu} előtt!')
        if index < len(szoveg) - 1 and szoveg[index+1] != ' ':
            print(f'Hiányzó szóköz {betu} után!')