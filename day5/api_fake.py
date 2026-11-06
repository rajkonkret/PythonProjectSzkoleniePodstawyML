import requests

produkt = {
    "title": "Plecak szkolny",
    "price": 79.99,
    "description": "Czarny plecak z kieszenią na laptopa",
    "category": "men's clothing",
    "image": "https://example.com/plecak.jpg",
}

odpowiedz = requests.post(
    "https://fakestoreapi.com/products",
    json=produkt,
    timeout=10,
)

print("Kod HTTP:", odpowiedz.status_code)
odpowiedz.raise_for_status()

dane = odpowiedz.json()
print(dane)
print("ID produktu:", dane["id"])
print("Nazwa:", dane["title"])
