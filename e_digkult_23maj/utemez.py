import os.path

# 1. feladat
taborok = []
with open(os.path.join(os.path.curdir, "forras", "taborok.txt"), "rt") as forrasfajl:
    for sor in forrasfajl:
        sor_list = sor.strip().split('\t')

        tabor = {}
        tabor['kezdes'] = (int(sor_list[0]), int(sor_list[1]))
        tabor['vege'] = (int(sor_list[2]), int(sor_list[3]))
        tabor['diakok'] = sor_list[4]
        tabor['tema'] = sor_list[5]
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
max_resztvevo = max([len(t['diakok']) for t in taborok])
legnepszerubbek = [t for t in taborok if len(t['diakok']) == max_resztvevo]
print("Legnépszerűbbek:")
for leg in legnepszerubbek:
    print(f"{leg['kezdes'][0]} {leg['kezdes'][1]} {leg['tema']}")

# 5. feladat
def sorszam(honap: int, nap: int) -> int:
    if honap == 6:
        return nap - 15
    elif honap == 7:
        return 15 + nap
    else:
        return 15 + 31 + nap

### Általánosabb megoldás, ahol a kezdeti feltételek szabadon módosíthatóak
# def sorszam(honap: int, nap: int) -> int:
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
ho = int(input("hó: "))
nap = int(input("nap: "))
napok = sorszam(ho, nap)
# print(f"Napok száma: {napok}")
meg_tart = [t for t in taborok
            if sorszam(t['kezdes'][0], t['kezdes'][1])
            <= napok <= sorszam(t['vege'][0], t['vege'][1])]
print(f"Ekkor éppen {len(meg_tart)} tábor tart.")

# 7. feladat
tanulo = input("Adja meg egy tanuló betűjelét: ")

tanulo_taborai = [t for t in taborok if tanulo in t['diakok']]
tanulo_taborai.sort(key=lambda tabor: sorszam(tabor['kezdes'][0], tabor['kezdes'][1]))
tabor_utkozes = False

with open(os.path.join(os.path.curdir, "egytanulo.txt"), "wt", encoding="utf-8") as celfajl:
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
