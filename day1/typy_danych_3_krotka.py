# krotka (tuple) - kolekcja tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jako stałą - szczególny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

# tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

# pep8
tupla_jeden = (45,)  # pep8 zaleca nawiasy dla tupli jednoelementowych
# tupla_jeden = 45,
print(tupla_jeden)
print(type(tupla_jeden))

del tupla_jeden  # usunięcie całej tupli
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined

# tupla_liczby[0] = 123  # TypeError: 'tuple' object does not support item assignment
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

print(tupla_imiona.index("Radek"))  # indeks 2
print(tupla_imiona.count("Radek"))  # występuje 1 raz

print(len(tupla_imiona))  # długość 4

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwszy, b - drugi element
a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie tupli
c, d = tup
print(c, d)  # 1 2

print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')
# name1, name2, name3

# ValueError: too many values to unpack (expected 3, got 4)
# name1, name2, name3 = tupla_imiona

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Zenek Marek ['Radek', 'Ania']

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Zenek', 'Marek'] Radek Ania

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Zenek ['Marek', 'Radek'] Ania

# sorted() - sortowanie, zwraca nową listę
print(sorted(tupla_imiona))
# ['Ania', 'Marek', 'Radek', 'Zenek']
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania') oryginał bez zmian

lista = list(tupla_imiona)
print(lista)  # ['Zenek', 'Marek', 'Radek', 'Ania']
