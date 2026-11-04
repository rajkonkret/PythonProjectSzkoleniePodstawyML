# funkcja - fragment kodu, który możemy wykonac w dowolnym momencie

# zdefiniowanie funkcji
def przedstaw_sie():  # funkcja bezargumentowa
    print("Cześć")


# uzycie funkcji
przedstaw_sie()  # Cześć


def dodaj_dwa(liczba):  # ma jeden obowiązkowy argument
    return liczba + 2  # zwróc wynik


# dodaj_dwa() # TypeError: dodaj_dwa() missing 1 required positional argument: 'liczba'
dodaj_dwa(2)  # nie wypisuje wyniku

print(dodaj_dwa(4))  # 6

wynik = dodaj_dwa(6)
print(wynik)
print(wynik)
print(wynik)  # 8


def dodaj(a=0, b=0):
    print(a + b)


# po pozycji
dodaj()
dodaj(1)
dodaj(11, 5)
# 0
# 1
# 16

# argumenty po nazwie
dodaj(b=10, a=8)  # 18


# funkcje ktora przyjmuje dowolna liczbę argumentów pozycyjnych
def nowa_lista(*args):
    lista1 = []
    lista1.extend(args)
    return lista1


print(nowa_lista(4, 5, 6, 7, 8, 9, 10, 11, 23, 45))


# [4, 5, 6, 7, 8, 9, 10, 11, 23, 45]

def all_par(*args, **kwargs):
    print(args, kwargs)


all_par(1, 2, 3, 4, 5, a=10, b=89, c=90)


# (1, 2, 3, 4, 5) {'a': 10, 'b': 89, 'c': 90}

# funkcje lambda
def dodaj(a=0, b=0):
    print(a + b)


dodaj_2 = lambda a, b: a + b  # return domyślnie
print(dodaj_2(4, 7))  # 11

lista = [2, 3, 7, 8, 90, 23, 45]
# przemnożyc przez 2 wszystkie elementy
print([i * 2 for i in lista])

# map() - funkcja wyższego rzedu, jako arg ma funkcje
# lambda jako funkcja anonimowa
print(list(map(lambda a: a * 2, lista)))
# [4, 6, 14, 16, 180, 46, 90]

# filter(), reduce()