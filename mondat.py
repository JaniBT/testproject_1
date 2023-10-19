print('A program a mondatvégi írásjelből kitalálja minden mondatot írtál!\n')
mondat = input('Adj meg egy mondatot: ')

if mondat[-1] == '!':
    print('A mondat felszólító/óhajtó/felkiáltó mondat.')
elif mondat[-1] == '?':
    print('A mondat kérdő mondat')
elif mondat[-1] == '.':
    print('A mondat kijelentő mondat')
else:
    print('Nem adtál meg mondatvégi írásjelet!')

