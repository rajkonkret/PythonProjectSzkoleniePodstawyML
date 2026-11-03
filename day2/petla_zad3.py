# while - pętla sterowana warunkiem

# pętla nieskońćzona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(50 * "-")

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

liczby = []
liczby_int = []
while True:

    liczba = input("Wprowadz liczbę całkowitą: ")

    # A string is numeric if all characters in the string are numeric
    if liczba.isnumeric():
        liczby.append(liczba)
        liczby_int.append(int(liczba))
    else:
        break

print(liczby)
print(liczby_int)
# Wprowadz liczbę całkowitą: 6
# Wprowadz liczbę całkowitą: 444
# Wprowadz liczbę całkowitą: 234235435
# Wprowadz liczbę całkowitą: a
# ['6', '444', '234235435']
# ['1', '2', '3']
# [1, 2, 3]
