""" Ütemezés (2023.05.22)
"""

# 1. feladat
from pathlib import Path

taborok = []

fajl = Path("forras","taborok.txt")
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split('\t')

        tabor = {
            'kezdes': (int(adatok[0]), int(adatok[1])),
            'vege': (int(adatok[2]), int(adatok[3])),
            'diakok': adatok[4],
            'tema': adatok[5],
        }
        taborok.append(tabor)

# 2. feladat
print("2. feladat")

print(f"Az adatsorok száma: {len(taborok)}")
print(f"Az először rögzített tábor témája: {taborok[0]['tema']}")
print(f"Az először rögzített tábor témája: {taborok[-1]['tema']}")

# 3. feladat
print("3. feladat")

zenei_taborok = [t for t in taborok if t['tema'] == "zenei"]

if len(zenei_taborok):
    for tabor in zenei_taborok:
        print(f"Zenei tábor kezdődik {tabor['kezdes'][0]}. hó {tabor['kezdes'][1]}. napján.")
else:
    print("Nem volt zenei tábor.")

# 4. feladat
print("4. feladat")

max_resztvevo = max(len(t['diakok']) for t in taborok)
legnepszerubbek = [t for t in taborok if len(t['diakok']) == max_resztvevo]

print("Legnépszerűbbek:")
for leg in legnepszerubbek:
    print(f"{leg['kezdes'][0]} {leg['kezdes'][1]} {leg['tema']}")

# 5. feladat
def sorszam(honap: int, nap: int) -> int:
    """ A függvény megadja, hogy a paraméterként kapott hónap és nap a nyári szünet hányadik napja
    """
    if honap == 6:
        hanyadik_nap = nap - 15
    elif honap == 7:
        hanyadik_nap = 15 + nap
    else:
        hanyadik_nap = 15 + 31 + nap
    return hanyadik_nap

## Általánosabb megoldás, ahol a kezdeti feltételek szabadon módosíthatóak
# def sorszam(honap: int, nap: int) -> int:
#     """ A függvény megadja, hogy a paraméterként kapott hónap és nap a nyári szünet hányadik napja
#     """
#     elso_honap = 6
#     elso_nap = 16
#     ho_napok = (30, 31, 31)
#
#     napok = 0
#     ho = honap - elso_honap
#     i = 0
#     while i < ho:
#         napok += (ho_napok[i] if i > 0 else ho_napok[i] - elso_nap + 1)
#         i += 1
#     napok += (nap if ho > 0 else nap - elso_nap + 1)
#     return napok

# 6. feladat
print("6. feladat")

be_honap = int(input("hó: "))
be_nap = int(input("nap: "))
# be_honap = 8
# be_nap = 1

napok = sorszam(be_honap, be_nap)
meg_tart = [t for t in taborok
            if sorszam(t['kezdes'][0], t['kezdes'][1])
            <= napok <= sorszam(t['vege'][0], t['vege'][1])]

print(f"Ekkor éppen {len(meg_tart)} tábor tart.")

# 7. feladat
tanulo = input("Adja meg egy tanuló betűjelét: ")
# tanulo = "L"

tanulo_taborai = [t for t in taborok if tanulo in t['diakok']]
tanulo_taborai.sort(key=lambda tabor: sorszam(tabor['kezdes'][0], tabor['kezdes'][1]))

tabor_utkozes = False

fajl = Path("egytanulo.txt")
with fajl.open("w", encoding="utf-8") as celfajl:
    for i, tabor in enumerate(tanulo_taborai):
        celfajl.write(
            f"{tabor['kezdes'][0]}.{tabor['kezdes'][1]}-"
            + f"{tabor['vege'][0]}.{tabor['vege'][1]}. "
            + f"{tabor['tema']}\n"
        )
        
        if i == 0:
            elozo_vege = sorszam(tabor['vege'][0], tabor['vege'][1])
        else:
            kezdet = sorszam(tabor['kezdes'][0], tabor['kezdes'][1])
            if elozo_vege >= kezdet:
                tabor_utkozes = True
            elozo_vege = sorszam(tabor['vege'][0], tabor['vege'][1])

if tabor_utkozes:
    print("Nem mehet el mindegyik táborba.")
else:
    print("Elmehet mindegyik táborba.")
