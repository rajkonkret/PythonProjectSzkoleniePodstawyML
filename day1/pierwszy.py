# rajkonkret660@gmail.com
# https://naukapythona.pl
# https://api.chucknorris.io/
print()  # wypisz/wydrukuj

print("Witaj Świecie")
print('Witaj Świecie')

# Witaj Świecie
# Witaj Świecie

# ctrl / - komentarz
# print('Radek")
# C:\Users\CSComarch\PycharmProjects\PythonProjectSzkoleniePodstawyML\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonProjectSzkoleniePodstawyML\day1\pierwszy.py
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectSzkoleniePodstawyML\day1\pierwszy.py", line 9
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 9)
#
# Process finished with exit code 1 - program wykonany z błedu

print("Dalsza częśc")  # Dalsza częśc

# ctrl d - powielanie linii
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")

# type() - sprawdzanie typu danych
print(type("Radek"))  # <class 'str'>, dane tekstowe

print("38" + "90")  # 3890, łaczenie tekstów, konkatenacj
print('Radek' + "1")  # Radek1

print(38 + 90)  # 128
print(type(90))  # <class 'int'>, liczby całkowite

# sys
import sys

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# print("28" + 89)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie typów: int(), str()
print(int("39") + int(30))  # 69
print("Radek" + str(1))  # Radek1

print(168 * "35")  # mnożenie tekstów

# zmienna - pudełko na dane, szufladka

# snake_case

name = "Radek"

print(name)
print(type(name))  # <class 'str'>

# typowane dynamiczne
age = 89
print(age)
print(type(age))  # <class 'int'>

age = "Radek"
print(age)
print(type(age))  # <class 'str'>

# print(age + 10)  # TypeError: can only concatenate str (not "int") to str

# podpowiedzi typów
name: str = "Radek"
print(name)
print(type(name)) # <class 'str'>

name = 90
print(name) # 90
# mypy, pyright, ruff