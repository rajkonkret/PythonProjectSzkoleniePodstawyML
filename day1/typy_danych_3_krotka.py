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
