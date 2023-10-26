""" Reklám (2023.10.25)
"""

# 1. feladat
from pathlib import Path

rendelesek = []

fajl = Path.cwd() / "forras" / "rendel.txt"
with fajl.open(encoding="ascii") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split()

        rendeles = {
            'nap': int(adatok[0]),
            'varos': adatok[1],
            'darab': int(adatok[2]),
        }
        rendelesek.append(rendeles)
# print(f"{rendelesek = }")

# 2. feladat
print("2. feladat")

print(f"A rendelések száma: {len(rendelesek)}")

# 3. feladat
print("3. feladat")

be_nap = int(input("Kérem, adjon meg egy napot: "))
# be_nap = 9

rendelesek_szama = sum((1 for r in rendelesek if r['nap'] == be_nap))
print(f"A rendelések száma az adott napon: {rendelesek_szama}")

# 4. feladat
print("4. feladat")

NAPOK_SZAMA = 30
napok_szama_nr = len({r['nap'] for r in rendelesek if r['varos'] == "NR"})

if napok_szama_nr < NAPOK_SZAMA:
    print(f"{NAPOK_SZAMA - napok_szama_nr} nap nem volt a reklámban nem érintett városból rendelés")
else:
    print("Minden nap volt rendelés a reklámban nem érintett városból")

# 5. feladat
print("5. feladat")

max_rendeles = max(rendelesek, key=lambda r: r['darab'])
print(f"A legnagyobb darabszám: {max_rendeles['darab']}, a rendelés napja: {max_rendeles['nap']}")

# 6. feladat
def osszes(osszes_rendeles: list[dict], varos_kod: str, nap_szama: int) -> int:
    """ A függvény megadja, hogy mennyi volt egy adott városból egy adott napon
    a rendelt termékek száma
    """
    return sum(r['darab'] for r in osszes_rendeles
               if r['varos'] == varos_kod and r['nap'] == nap_szama)

# 7. feladat
print("7. feladat")

ossz_pl = osszes(rendelesek, 'PL', 21)
ossz_tv = osszes(rendelesek, 'TV', 21)
ossz_nr = osszes(rendelesek, 'NR', 21)
print(f"A rendelt termékek darabszáma a 21. napon PL: {ossz_pl} TV: {ossz_tv} NR: {ossz_nr}")

# 8. feladat
print("8. feladat")

fajl = Path.cwd() / "kampany.txt"
with fajl.open("w", encoding="utf-8") as celfajl:
    fejlec = "Napok\t1..10\t11..20\t21..30\n"
    print(fejlec, end="")
    celfajl.write(fejlec)

    for v in ("PL", "TV", "NR"):
        szum1 = sum(1 for r in rendelesek if r['varos'] == v and 1 <= r['nap'] <= 10)
        szum2 = sum(1 for r in rendelesek if r['varos'] == v and 11 <= r['nap'] <= 20)
        szum3 = sum(1 for r in rendelesek if r['varos'] == v and 21 <= r['nap'] <= 30)
        
        sor = f"{v}\t{szum1}\t{szum2}\t{szum3}\n"
        print(sor, end="")
        celfajl.write(sor)
