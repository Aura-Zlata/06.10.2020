"""
Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane, exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. 
Exemplu : Date de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani.
"""


import datetime

datc= datetime.datetime.now()
ac=datc.year
lc=datc.month
zc=datc.day

an=int(input("Introduceti anul nasterii:"))
ln=int(input("Introduceti locul nasterii:"))
zc=int(input("Introduceti ziua nasterii:"))

if (an<=ac or (an==an and ((ln<=lc and zc<zc) or (ln<lc and zc>=zc)))) and ac-an<135:
    if (lc<=ln and zc<zc and ac>an)
        print(ac-an-1,"ani")
    elif lc==ln and zc==an and ac>an:
        print("La multi ani, ai implinit", ac-an,"ani")
    elif (lc>=ln and zc>zn) or (lc>ln and zc<=zn):
        print(ac-an, "ani")
    else: print("Error:Data nasterii nu este corecta")