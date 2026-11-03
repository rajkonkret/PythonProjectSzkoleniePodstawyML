# napisać kalkulator
# while True
# menu z opcjami
# wyświetlić ładnie wynik -> f-string -> 5 * 8 = 40
# obsłużyc wyjątki

while True:
    # print("Tu będzie menu")
    print("""
    1. Dodawanie
    2. Odejmowanie
    5. Koniec
    """)

    odp = input("Wybierz opcję z menu: ")

    # if odp == "5":
    #     break
    if odp not in ['1', '2']:
        break