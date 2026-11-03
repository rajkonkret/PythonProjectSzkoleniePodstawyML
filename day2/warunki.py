# instrukcje warunkowe
# instrukcje sterowania przepywem programu

# if
# w zależności od warunku wykona jeden lub drugi blok programu
# wyrażenie w warunku musi zwróci bool
# bool()

odp = True
print(bool(odp))  # True

if odp: print('test')  # test

if odp:
    print("Test")  # Test
print(50 * "-")

# debugger - narzędzie do wykonywania kodu krok po kroku
# pułapka
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("koniec warunku")

# odp = "Radek"
odp = "Tomek"
if odp == "Radek":
    print("Jestem Radek")
else:
    print("To nie Radek")
# To nie Radek

if odp == "Radek":
    print("Jestem Radek")
elif odp == "Tomek":
    print("Jestem Tomek")
else:
    print("inny")
# Jestem Tomek

# pobieramy od użytkownika liczbę od 0 do 100
# jesli wynik egzaminu 90 i wiecej -> bardzo dobry
# od 60 do 89 -> zdany
# ponizej 60 -> niezdany
#
# punkty = int(input("Podajliczbę punktów: "))
#
# if punkty >= 90:
#     print("Bardzo dobry")
# elif punkty >= 60:
#     print("Egzamin zdany")
# else:
#     print("Egzamin niezdany")
# # Podajliczbę punktów: 60
# # Egzamin zdany

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")

# operator warunkowy
rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")
# Rabat wynosi: 25
# Rabat wynosi: 25

# napisac test z...
# trzy patania
# puntacja
punkty = 0

odp = input("Która drużyna wygrała Mundial 2026: ")
if odp.strip().casefold() == "Hiszpania".strip().casefold():
    print("Odpowiedź prawidłowa")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Zła odpowiedź")

odp = input("Jaki jest Król na banknocie 200 zł: ")
if odp.strip().casefold() == "Zygmunt".strip().casefold():
    print("Odpowiedź prawidłowa")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Zła odpowiedź")

print("Punkty:", punkty)

# Która drużyna wygrała Mundial 2026: Hiszpania
# Odpowiedź prawidłowa
# Jaki jest Król na banknocie 200 zł: Zygmunt
# Odpowiedź prawidłowa
# Punkty: 2
