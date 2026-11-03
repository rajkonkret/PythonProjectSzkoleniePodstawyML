dictionary = {"imie": "Radek", "nazwisko": "Kowalski"}

# klucze, wartości, par

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wypisze wartości
for k in dictionary.values():
    print(k)
# Radek
# Kowalski

# wypisze pary
for i in dictionary.items():
    print(i)
    # ('imie', 'Radek')
    # ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "<==>", v)
# imie <==> Radek
# nazwisko <==> Kowalski

for k, v in dictionary.items():
    print(k, v, sep="-ooo-")
# imie-ooo-Radek
# nazwisko-ooo-Kowalski

for k, v in dictionary.items():
    print(k, v, sep="-ooo-", end=" | | ")
# imie-ooo-Radek | | nazwisko-ooo-Kowalski | |
