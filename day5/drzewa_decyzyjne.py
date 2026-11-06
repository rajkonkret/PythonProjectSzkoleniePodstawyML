from matplotlib import pyplot as plt

dane = [
    {"wiek": 55, "zarobki": 70, "decyzja": "tak"},
    {"wiek": 53, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 47, "zarobki": 60, "decyzja": "tak"},
    {"wiek": 40, "zarobki": 30, "decyzja": "nie"},
    {"wiek": 35, "zarobki": 45, "decyzja": "tak"},
    {"wiek": 28, "zarobki": 65, "decyzja": "nie"},
    {"wiek": 31, "zarobki": 42, "decyzja": "tak"},
    {"wiek": 29, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 52, "zarobki": 80, "decyzja": "tak"},
    {"wiek": 60, "zarobki": 55, "decyzja": "tak"},
]


# indeks giniego
# entropia - logarytmiczna - wolniejsza

def gini_index(dane):
    total = len(dane)
    if total == 0:
        return 0

    decyzje = [x['decyzja'] for x in dane]
    pozytywne = decyzje.count("tak") / total
    negatywne = decyzje.count("nie") / total

    gini = 1 - (pozytywne ** 2 + negatywne ** 2)

    return gini


def gini_po_podzialu(lewa, prawa):
    total = len(lewa) + len(prawa)
    w1 = len(lewa) / total
    w2 = len(lewa) / total

    return w1 * gini_index(lewa) + w2 * gini_index(prawa)


def wypisz_grupe(nazwa, grupa):
    print(f"\n {nazwa} (liczba {len(grupa)}")
    print(f" tak:", sum(1 for x in grupa if x['decyzja'] == 'tak'))
    print(f" nie:", sum(1 for x in grupa if x['decyzja'] == 'nie'))
    print(f" Gini: {round(gini_index(grupa), 3)}")


# dzielimy wg wieku > 50
wiek_value = 50
wiek_lewo = [x for x in dane if x['wiek'] > wiek_value]
wiek_prawo = [x for x in dane if x['wiek'] <= wiek_value]

print("Gini (całosc)", round(gini_index(dane), 3))
print("Gini po podziale (wiek >50)", round(gini_po_podzialu(wiek_lewo, wiek_prawo), 3))
# Gini (całosc) 0.48
# Gini po podziale (wiek >50) 0.35

zarobki_value = 50
zarobki_lewo = [x for x in dane if x['zarobki'] > zarobki_value]
zarobki_prawo = [x for x in dane if x['zarobki'] <= zarobki_value]

print("Gini (całosc)", round(gini_index(dane), 3))
print("Gini po podziale (zarobki >50)", round(gini_po_podzialu(zarobki_lewo, zarobki_prawo), 3))

# Gini (całosc) 0.48
# Gini po podziale (wiek >50) 0.4
