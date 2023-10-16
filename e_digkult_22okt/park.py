from pathlib import Path

# 1. feladat
felajanlasok = []
with open(Path("forras","felajanlas.txt"), "rt") as forrasfajl:
    agyasok_szama = int(forrasfajl.readline().strip())
    for sor in forrasfajl:
        adatok = sor.strip().split()
        
        felajanlas = {
            'elso': int(adatok[0]),
            'utolso': int(adatok[1]),
            'szin': adatok[2],
        }
        felajanlasok.append(felajanlas)

# 2. feladat
print("2. feladat")

print(f"A felajánlások száma: {len(felajanlasok)}\n")

# 3. feladat
print("3. feladat")

bejarat_ultetok = [str(i + 1) for i, f in enumerate(felajanlasok)
                   if f['elso'] > f['utolso'] or (f['elso'] == 1 and f['utolso'] == agyasok_szama)]

print(f"A bejárat mindkét oldalán ültetők: {' '.join(bejarat_ultetok)}\n")

# 4. feladat
print("4. feladat")

sorszam = int(input("Adja meg az ágyás sorszámát! "))

talalat = 0
ultetes_osszes = []
for felajanlas in felajanlasok:
    if felajanlas['elso'] > felajanlas['utolso']:
        agyas_sorszamok = [x for x in range(1, felajanlas['utolso'] + 1)]
        agyas_sorszamok += [x for x in range(felajanlas['elso'], agyasok_szama + 1)]
    else:
        agyas_sorszamok = [x for x in range(felajanlas['elso'], felajanlas['utolso'] + 1)]
    felajanlas['agyasok'] = agyas_sorszamok
    if (sorszam in felajanlas['agyasok']):
        talalat += 1
        ultetes_osszes.append(felajanlas['szin'])

print(f"A felajánlók száma: {talalat}")

if len(ultetes_osszes) > 0:
    print(f"A virágágyás színe, ha csak az első ültet: {ultetes_osszes[0]}")
    szinek = set([szin for szin in ultetes_osszes])
    print(f"A virágágyás színei: {' '.join(szinek)}\n")
else:
    print("Ezt az ágyást nem ültetik be.\n")

# 5. feladat
print("5. feladat")

ultetesek = [False for _ in range(agyasok_szama)]

osszes_ultetes = 0
for felajanlas in felajanlasok:
    for i in felajanlas['agyasok']:
        ultetesek[i - 1] = True
    osszes_ultetes += len(felajanlas['agyasok'])

if ultetesek.count(True) == agyasok_szama:
    print("Minden ágyás beültetésére van jelentkező.")
elif osszes_ultetes >= agyasok_szama:
    print("Átszervezéssel megoldható a beültetés.")
else:
    print("A beültetés nem oldható meg.")

# 6. feladat
ultetesek = [['#', 0] for _ in range(agyasok_szama)]
for sorszam, felajanlas in enumerate(felajanlasok, start = 1):
    for i in felajanlas['agyasok']:
        if ultetesek[i - 1][0] == '#':
            ultetesek[i - 1][0] = felajanlas['szin']
            ultetesek[i - 1][1] = sorszam

with open(Path("szinek.txt"), "wt", encoding="utf-8") as celfajl:
    for ultetes in ultetesek:
        celfajl.write(f"{ultetes[0]} {ultetes[1]}\n")
