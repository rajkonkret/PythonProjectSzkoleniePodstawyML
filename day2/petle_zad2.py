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

pol_ang = {'pies': "dog", "kot": "cat", "dach": "roof"}
# zrobic ang_pol

print()
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k

print(ang_pol)
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

# dict comprehensions
print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}
