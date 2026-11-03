# zbiór (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie ma indeksu
# hashowany

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} zmiana kolejności
