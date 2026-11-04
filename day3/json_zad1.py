# json - dane typu klucz - wartosc
# typ wymiany danych pomiędzy klient serwer
# odpowiednikiem jsona w pythonie jest słownik
# zawsze podwójne cudzysłowia
# None -> null

# orjson
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))
print(person_dict)
# {'name': 'Radek', 'age': 40, 'czy_pali': None}

# zapis danych jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }


with open('nasze_dane.json', "r") as file:
    data = json.load(file)

print(data)
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>

print(data['name'])  # Radek

# zamiana słownika na json
json_text = json.dumps(data)
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_text))  # <class 'str'>

# zamiana jsona na słownik
dict_json = json.loads(json_text)
print(dict_json)
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>

print("Imię pacjenta:", dict_json['name'])
# Imię pacjenta: Radek
