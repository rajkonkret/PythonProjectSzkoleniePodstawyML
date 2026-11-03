# pętla - wykonanie kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic ie rób

print(i)  # 19

for i in range(5, 15):  # od 5 do 14
    print(i)

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    print(_)

lista3 = []
for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
        lista3.append(i)
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

# wypisac elementy z za pomocą for
for i in range(len(lista3)):
    print(f"Wartośc: {lista3[i]}")
# Wartośc: 0
# Wartośc: 2
# Wartośc: 4
# Wartośc: 6
# Wartośc: 8

for c in lista3:  # pod c znajdzie sie element
    print(c)

lista_nazwy = ["Ala", "Tomek", "Zenek", 'Basia']

# 0 Ala
for p in lista_nazwy:
    print(lista_nazwy.index(p), p)

# enumerate() - zwraca/nadaje numer i element kolekcji
for p in enumerate(lista_nazwy):
    print(p)
# (0, 'Ala')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Basia') -> 3 Basia

a, b = (3, 'Basia')
print(a, b)  # 3 Basia

for i, o in enumerate(lista_nazwy):
    print(i, o)
# 0 Ala
# 1 Tomek
# 2 Zenek
# 3 Basia

for i, o in enumerate(lista_nazwy, start=1):
    print(i, o)
    # 2 Tomek
    # 3 Zenek
    # 4 Basia

lista_nazwy = ["Ala", "Tomek", "Zenek", 'Basia']
wiek = [24, 18, 34, 20]

# Ala 24
for i in range(len(lista_nazwy)):
    print(f"{lista_nazwy[i]}, {wiek[i]}")

# Ala, 24
# Tomek, 18
# Zenek, 34
# Basia, 20

lista_nazwy = ["Ala", "Tomek", "Zenek", 'Basia', 'Marek']
wiek = [24, 18, 34, 20]

# zip() - łaczy kolekcje
for i in zip(lista_nazwy, wiek):
    print(i)
# ('Ala', 24)
# ('Tomek', 18)
# ('Zenek', 34)
# ('Basia', 20)

# ValueError: zip() argument 2 is shorter than argument 1
# for o, w in zip(lista_nazwy, wiek, strict=True):
for o, w in zip(lista_nazwy, wiek):
    print(o, w)
# Ala 24
# Tomek 18
# Zenek 34
# Basia 20

# praca domowe
# zip_longest
# 0 Ala 24
