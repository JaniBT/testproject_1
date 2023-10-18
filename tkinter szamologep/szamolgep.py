import math


    try:
            print("\n================================ (ENTER leütésével léphetsz ki)")
            print("Adj meg egy számot: ")
            szam1 = int(input())
            print("Adj meg egy másik számot: ")
            szam2 = int(input())
            print("Add meg, hogy kivonni, összeadni, szorozni vagy osztani szeretnéd: ")
            muveletijel = input()
            while szam1 != "q":
                if szam1 != int or szam2 != int or muveletijel != "*" or muveletijel != "/" or muveletijel != "+" or muveletijel != "-":
                    if muveletijel == "+":
                        print(f'Az eredmény: {szam1+szam2}')
                    elif muveletijel == "-":
                        print(f'Az eredmény: {szam1-szam2}')
                    elif muveletijel == "*":
                        print(f'Az eredmény: {szam1*szam2}')
                    else:
                        print(f'Az eredmény: {szam1/szam2}')
                        
                    print("\n================================ (ENTER leütésével léphetsz ki)")
                    print("Adj meg egy számot: ")
                    szam1 = int(input())
                    print("Adj meg egy másik számot: ")
                    szam2 = int(input())
                    print("Add meg, hogy kivonni, összeadni, szorozni vagy osztani szeretnéd: ")
                    muveletijel = input()
    except ValueError:
            print("Csak adott karaktereket adhatsz meg!")