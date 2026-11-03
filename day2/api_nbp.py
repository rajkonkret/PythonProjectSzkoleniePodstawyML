# rest api - wymina danych pomiedzy systemami. za ppomocą metod http
# GET, POST, PUT, PATCH, DELETE, HEAD
# json, xml

# klient http
import requests

# pip
# pip install requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

data = requests.get(url)
print(data)  # <Response [200]>
# 200 ok
# 3xx warningi, przekierowania
# 4xx -> 404 brak strony, 400 Bad Request
# 5xx -> 500 Internal Server Error

response = data.text
print(response)
print(type(response))  # <class 'str'>

response = data.json()  # zamiana jsona na słownik
print(response)
# {'table': 'A',
# 'currency': 'euro',
# 'code': 'EUR',
# 'rates': [{'no': '213/A/NBP/2026', 'effectiveDate': '2026-11-02', 'mid': 4.4185}]}
print(type(response))  # <class 'dict'>

# nazwa waluty i jaki kurs dzisiaj
print("Waluta:", response['currency'])  # Waluta: euro
print("Kurs:", response['rates'][0]['mid'])  # Kurs: 4.4185
