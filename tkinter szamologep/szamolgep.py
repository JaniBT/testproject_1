import math

status = True
while status:
    try:
            print("\n================================ (69 leütésével léphetsz ki)")
            print("Adj meg egy számot: ")
            szam1 = int(input())
            print("Adj meg egy másik számot: ")
            szam2 = int(input())
            print("Add meg, hogy kivonni, összeadni, szorozni vagy osztani szeretnéd: ")
            muveletijel = input()
            if szam1 != "q":
                while szam1 != "q":
                    if szam1 != int or szam2 != int or muveletijel != "*" or muveletijel != "/" or muveletijel != "+" or muveletijel != "-":
                        if muveletijel == "+":
                            print(f'Az eredmény: {szam1+szam2}')
                        elif muveletijel == "-":
                            print(f'Az eredmény: {szam1-szam2}')
                        elif muveletijel == "*":
                            print(f'Az eredmény: {szam1*szam2}')
                        elif muveletijel == "/":
                            print(f'Az eredmény: {szam1/szam2}')
                        else:
                            print('Csak adott műveleti jelet adhatsz meg! (+, -, *, /)')
                    elif szam1 == "q":
                        status = False
            elif szam1 == "q":
                status = False
                print(status)
    except ValueError:
            print("Csak adott karaktereket adhatsz meg!")