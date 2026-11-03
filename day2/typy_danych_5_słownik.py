# słownik - para {klucz : waartość}
# {"user" : "Radek"}
# klucze nie mogą się powtarzać

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dict_1 = dict()
print(dict_1)  # {}
print(type(dict_1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodac klucze
dictionary['wiek'] = 54
print(dictionary)  # {'imie': 'Radek', 'wiek': 54}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 54])
# dict_items([('imie', 'Radek'), ('wiek', 54)])

# nadpisanie wartości
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 54}

# wypisanie
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ['Radek', "Tomek", "Anna"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Anna'], 'wiek': 54}

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # ['Radek', 'Tomek', 'Anna']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

dictionary.update({'date': '12-12-2067'})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Anna'], 'wiek': 54, 'date': '12-12-2067'}

# [('imie', 'Radek'), ('wiek', 54)]

dict_small = {'x': 20}
print(dict_small)
dict_small.update([('imie', 'Radek'), ('wiek', 54)])
print(dict_small)  # {'x': 20, 'imie': 'Radek', 'wiek': 54}

# input() - mozliwosc wprowadzania danych do komputera
# tekst = input("Podaj imię: ")
# print(tekst)
# Podaj imię: Radek
# Radek

# napisac aplikację kalkulator
# a + b
a = int(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
print(int(a) + float(b))
# Podaj liczbę a: 5
# Podaj liczbę b: 6
# 11.0
