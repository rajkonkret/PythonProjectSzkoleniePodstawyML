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
