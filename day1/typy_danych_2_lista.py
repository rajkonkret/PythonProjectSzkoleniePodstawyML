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
