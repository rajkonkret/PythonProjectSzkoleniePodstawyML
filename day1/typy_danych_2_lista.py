# kolekcja

# lista - zachowuje kolejność, pozwala przechowywwac dowolną ilośc danych, różnego typu na raz

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie lementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Adrian")
lista.append("Jarek")
lista.append("Karol")
lista.append("Zenek")
lista.append("Anna")
print(lista)
# ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']

print(len(lista))  # długośc 7

# ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']
#     0         1        2         3        4       5        6

print(lista[0])
print(lista[2])
print(lista[4])
# Radek
# Adrian
# Karol

# print(lista[10])  # IndexError: list index out of range

# ostatni element z listy
print(lista[len(lista) - 1])  # Anna
print(lista[-1])  # Anna

# ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']
#     0         1        2         3        4       5        6
#     -7        -6       -5        -4       -3      -2       -1

print(lista[-2])  # Zenek

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Adrian'] indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Adrian']

print(lista[2:])  # ['Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna'] włacznie z ostatnim
print(lista[2:6])  # ['Adrian', 'Jarek', 'Karol', 'Zenek'] bez ostatniego

print(lista[2:7])  # ['Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']
print(lista[2:10])  # ['Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']

print(lista[15:20])  # []

print(lista[:])
# ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']

# ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']
#     0         1        2         3        4       5        6
#     -7        -6       -5        -4       -3      -2       -1

print(lista[-2:0])  # [5:0] # []
print(lista[0:-2])  # [0:5] ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol']

a = None
b = None
print(lista[a:b])
print(lista[None:None])
# ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']

# wygenerowac listę int z zakresu 0 do 14
# lista_15 = [0,1,2...]
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14] [start:stop:krok]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(lista_15[::-1])  # odwrócona kolejność
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(list(range(5, 15, 2)))  # [5, 7, 9, 11, 13] (start, stop, krok)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2)  # [1, 2, 3, 4, 5, 6] łaczy listy

lista_range = list(range(5, 9))
lista1.append(lista_range)
print(lista1)  # [1, 2, 3, [5, 6, 7, 8]]

lista2.extend(lista_range)
print(lista2)  # [4, 5, 6, 5, 6, 7, 8]

# nie ma typu tablica (array)
tablica = [[1, 2], [3, 4]]
print(tablica)
# numpy - biblioteka do działań z tablicami/macierzami

print(lista)
# ['Radek', 'Tomek', 'Adrian', 'Jarek', 'Karol', 'Zenek', 'Anna']

# nadpisanie danych
lista[2] = "Alicja"
print(lista)
# ['Radek', 'Tomek', 'Alicja', 'Jarek', 'Karol', 'Zenek', 'Anna']

# dopisanie elementu we wskazanym indeksie

lista.insert(1, "Ola")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Alicja', 'Jarek', 'Karol', 'Zenek', 'Anna']

# sprawdzenie indexu
print(lista.index("Alicja"))  # 3

# dopiszcie jakis elemnt
# sprawdzic index
lista.append("Jarek")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Alicja', 'Jarek', 'Karol', 'Zenek', 'Anna', 'Jarek']

print(lista.index("Jarek"))  # index numer 4

# usunięcie eleemntu z listy
lista.remove("Jarek")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Alicja', 'Karol', 'Zenek', 'Anna', 'Jarek']

# usunięcie po indeksie, zwraca usunięty element
# pop()
print(lista.pop(2))  # Tomek
print(lista)
# ['Radek', 'Ola', 'Alicja', 'Karol', 'Zenek', 'Anna', 'Jarek']

zmienna = lista.pop()  # usunie ostatni element
print(zmienna)  # Jarek

# typy proste
a = 1
b = 3
a = b
print(f"{a=}, {b=}")
# a=3, b=3

b = 9
print(f"{a=}, {b=}")
# a=3, b=9

b, a = a, b  # zamiana miejscacmi wartości zmiennych
print(b, a)  # 3 9

print(lista)
# ['Radek', 'Ola', 'Alicja', 'Karol', 'Zenek', 'Anna']

lista2 = lista  # kopia adresu, kopia referencji
print(lista)
# ['Radek', 'Ola', 'Alicja', 'Karol', 'Zenek', 'Anna']
print(lista2)
# ['Radek', 'Ola', 'Alicja', 'Karol', 'Zenek', 'Anna']

lista_copy = lista.copy()  # kopia elementów listy

lista.clear()  # usunięcie wszystkich elementów z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)
# ['Radek', 'Ola', 'Alicja', 'Karol', 'Zenek', 'Anna']

# id()
print(id(lista))  # 2393884323904
print(id(lista2))  # 2393884323904
print(id(lista_copy))  # 2393886894464

liczby = [54, 999, 12.34, 34, 567, 999]
print(type(liczby))  # <class 'list'>

# wypisac liczby
# nadpisac czwarty element inną liczby (czwarty po ludzku)
# wyciągnąć elementy od pierwszego do trzeciego włącznie
# wypisać po indeksie dodatnim i ujemnym

print(liczby)
liczby[3] = 666
print(liczby[1:3])
print(liczby[2])
print(liczby[-2])
# [54, 999, 12.34, 34, 567, 999]
# [999, 12.34]
# 12.34
# 567
