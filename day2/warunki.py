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

