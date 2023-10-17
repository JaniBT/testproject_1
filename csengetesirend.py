# Az órák kezdete és a csengetési idők
ora_kezdete = "08:00"
elso_csenges = "08:45"
masodik_csenges = "09:40"
harmadik_csenges = "10:35"
negyedik_csenges = "11:40"
otodik_csenges = "12:35"
hatodik_csenges = "13:30"
hetedik_csenges = "14:25"

diak_erkezese = input("Mikor érkeztél az órádra? (HH:MM formátumban): ")

try:
    ora_kezdete_percek = int(ora_kezdete[:2]) * 60 + int(ora_kezdete[3:])
    diak_erkezese_percek = int(diak_erkezese[:2]) * 60 + int(diak_erkezese[3:])
    
    keses_percekben = diak_erkezese_percek - ora_kezdete_percek
    
    if keses_percekben < 0:
        print("Nem késtél az óráról, korábban érkeztél.")
    elif keses_percekben == 0:
        print("Pontosan érkeztél az órádra.")
    elif keses_percekben <= 15:
        print(f"{keses_percekben} percet késtél az iskolából.")
    elif keses_percekben <= 45:
        print(f"{keses_percekben} percet késtél az iskolából.")
    elif keses_percekben <= 105:
        print(f"{keses_percekben} percet késtél az iskolából.")
    else:
        print(f"{keses_percekben} percet késtél az iskolából.")
except ValueError:
    print("Hibás formátum. Kérlek, használd a HH:MM formátumot.")
