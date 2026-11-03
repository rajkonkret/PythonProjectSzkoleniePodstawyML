# zbiór (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie ma indeksu
# hashowany

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} zmiana kolejności

# sorted()
sortowanie = sorted(zbior)  # zwróciło liste
print(sortowanie)  # [11, 22, 33, 44, 55, 66, 777]

# pusty zbiór
zb2 = set()  # tylko i wyłacznie słowko set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(24)
zbior.add(33)
zbior.add(25)
print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}

# usunięcie eleemntu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24, 25}

# pop() - usunięcie pierwszego
print(zbior.pop())
print(zbior)
# {66, 777, 11, 44, 18, 22, 24, 25}

zmienna = zbior.pop()
print(zmienna)  # 66

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior_2)
print(type(zbior_2))  # <class 'set'>

# operacje na zbiorach

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

# część wspólna zbiorów
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica zbiorów
print(zbior - zbior_2)  # {24, 777, 22, 25}
print(zbior.difference(zbior_2))  # {24, 777, 22, 25}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# zmienia bazowy
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}
