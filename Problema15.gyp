"""
Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. 
Radu este pe locul x în ordinea mediilor. 
În ce clasa va fi repartizat (A, B, C, D sau E)?. 
Exemplu : date de intrare : x=73 date de ieşire : C.
"""

x=int(input("Introduceti locul lui Radu:"))

if x<=125:
    if x>=98:
        print("E")
    elif x>=65:
        print("D")
    elif x>=50:
        print("C")
    elif x>=28:
        print("B")
    else:
        print("A")
else: print("Radu nu va fi in scoala")