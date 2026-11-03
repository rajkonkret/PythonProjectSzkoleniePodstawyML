# wyjątki - błedy wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectSzkoleniePodstawyML\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

lista = []

try:
    # print(5 / 0)
    # int("Q")
    # lista[1]
    # print(2 + "Ania")
    # raise KeyError("Bład klucza")
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except IndexError:
    print("Brak elementu na liście")
except Exception as e:
    print("Bład:", e)
else: # tylko gdy nie ma błędu
    print(wynik)
finally: # wykona się zawsze
    print("Kolejny element")

print("Program nadal działą")
